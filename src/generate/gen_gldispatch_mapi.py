#!/usr/bin/env python3

# Copyright (C) 2010 LunarG Inc.
# (C) Copyright 2015, NVIDIA CORPORATION.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
# Authors:
#    Kyle Brenneman <kbrenneman@nvidia.com>
#
# Based on code ogiginally by:
#    Chia-I Wu <olv@lunarg.com>


"""
Generates the glapi_mapi_tmp.h header file from Khronos's XML file.
"""

import sys
import xml.etree.cElementTree as etree

import genCommon

def _main():
    target = sys.argv[1]
    xmlFiles = sys.argv[2:]

    roots = [ etree.parse(filename).getroot() for filename in xmlFiles ]
    allFunctions = genCommon.getFunctionsFromRoots(roots)

    names = genCommon.getExportNamesFromRoots(target, roots)
    functions = [f for f in allFunctions if(f.name in names)]

    if (target in ("gl", "gldispatch")):
        assert(len(functions) == len(allFunctions))
        assert(all(functions[i] == allFunctions[i] for i in range(len(functions))))
        assert(all(functions[i].slot == i for i in range(len(functions))))

    print(r"""
/* This file is automatically generated by mapi_abi.py.  Do not modify. */

#ifndef _GLAPI_TMP_H_
#define _GLAPI_TMP_H_
typedef int GLclampx;
typedef void (APIENTRY  *GLDEBUGPROCKHR)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam);
#endif /* _GLAPI_TMP_H_ */
""".lstrip("\n"))

    print(generate_defines(functions))
    print(generate_table(functions, allFunctions))
    print(generate_noop_array(functions))
    print(generate_public_stubs(functions))
    print(generate_public_entries(functions))
    print(generate_stub_asm_gcc(functions))

def generate_defines(functions):
    text = r"""
#ifdef MAPI_TMP_DEFINES
#define GL_GLEXT_PROTOTYPES
#include "GL/gl.h"
#include "GL/glext.h"

""".lstrip("\n")
    for func in functions:
        text += "GLAPI {f.rt} APIENTRY {f.name}({f.decArgs});\n".format(f=func)
    text += "#undef MAPI_TMP_DEFINES\n"
    text += "#endif /* MAPI_TMP_DEFINES */\n"
    return text

def generate_table(functions, allFunctions):
    text = "#ifdef MAPI_TMP_TABLE\n"
    text += "#define MAPI_TABLE_NUM_STATIC %d\n" % (len(allFunctions))
    text += "#define MAPI_TABLE_NUM_DYNAMIC %d\n" % (genCommon.MAPI_TABLE_NUM_DYNAMIC,)
    text += "#undef MAPI_TMP_TABLE\n"
    text += "#endif /* MAPI_TMP_TABLE */\n"
    return text

def generate_noop_array(functions):
    text = "#ifdef MAPI_TMP_NOOP_ARRAY\n"
    text += "#ifdef DEBUG\n\n"

    for func in functions:
        text += "static {f.rt} APIENTRY noop{f.basename}({f.decArgs})\n".format(f=func)
        text += "{\n"
        if (len(func.args) > 0):
            text += "  "
            for arg in func.args:
                text += " (void) {a.name};".format(a=arg)
            text += "\n"
        text += "   noop_warn(\"{f.name}\");\n".format(f=func)
        if (func.hasReturn()):
            text += "   return ({f.rt}) 0;\n".format(f=func)
        text += "}\n\n"

    text += "const mapi_func table_noop_array[] = {\n"
    for func in functions:
        text += "   (mapi_func) noop{f.basename},\n".format(f=func)
    for i in range(genCommon.MAPI_TABLE_NUM_DYNAMIC - 1):
        text += "   (mapi_func) noop_generic,\n"
    text += "   (mapi_func) noop_generic\n"
    text += "};\n\n"
    text += "#else /* DEBUG */\n\n"
    text += "const mapi_func table_noop_array[] = {\n"
    for i in range(len(functions) + genCommon.MAPI_TABLE_NUM_DYNAMIC - 1):
        text += "   (mapi_func) noop_generic,\n"
    text += "   (mapi_func) noop_generic\n"

    text += "};\n\n"
    text += "#endif /* DEBUG */\n"
    text += "#undef MAPI_TMP_NOOP_ARRAY\n"
    text += "#endif /* MAPI_TMP_NOOP_ARRAY */\n"
    return text

def generate_public_stubs(functions):
    text = "#ifdef MAPI_TMP_PUBLIC_STUBS\n"

    text += "static const struct mapi_stub public_stubs[] = {\n"
    for func in functions:
        text += "   { \"%s\", %d, NULL },\n" % (func.name, func.slot)
    text += "};\n"
    text += "#undef MAPI_TMP_PUBLIC_STUBS\n"
    text += "#endif /* MAPI_TMP_PUBLIC_STUBS */\n"
    return text

def generate_public_entries(functions):
    text = "#ifdef MAPI_TMP_PUBLIC_ENTRIES\n"

    for func in functions:
        retStr = ("return " if func.hasReturn() else "")
        text += r"""
GLAPI {f.rt} APIENTRY {f.name}({f.decArgs})
{{
   const struct _glapi_table *_tbl = entry_current_get();
   mapi_func _func = ((const mapi_func *) _tbl)[{f.slot}];
   {retStr}(({f.rt} (APIENTRY *)({f.decArgs})) _func)({f.callArgs});
}}

""".lstrip("\n").format(f=func, retStr=retStr)

    text += "\n"
    text += "static const mapi_func public_entries[] = {\n"
    for func in functions:
        text += "   (mapi_func) %s,\n" % (func.name,)
    text += "};\n"
    text += "#undef MAPI_TMP_PUBLIC_ENTRIES\n"
    text += "#endif /* MAPI_TMP_PUBLIC_ENTRIES */\n"
    return text

def generate_stub_asm_gcc(functions):
    text = "#ifdef MAPI_TMP_STUB_ASM_GCC\n"
    text += "__asm__(\n"

    for func in functions:
        text += 'STUB_ASM_ENTRY("%s")"\\n"\n' % (func.name,)
        text += '"\\t"STUB_ASM_CODE("%d")"\\n"\n\n' % (func.slot,)

    text += ");\n"
    text += "#undef MAPI_TMP_STUB_ASM_GCC\n"
    text += "#endif /* MAPI_TMP_STUB_ASM_GCC */\n"
    return text

if (__name__ == "__main__"):
    _main()

