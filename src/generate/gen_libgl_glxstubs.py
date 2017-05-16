#!/usr/bin/env python3

# (C) Copyright 2015, NVIDIA CORPORATION.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# on the rights to use, copy, modify, merge, publish, distribute, sub
# license, and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  IN NO EVENT SHALL
# IBM AND/OR ITS SUPPLIERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# Authors:
#    Kyle Brenneman <kbrenneman@nvidia.com>

"""
Generates src/GL/g_libglglxwrapper.c from Khronos's glx.xml file.

This script generates stubs for every known extension function as well.
"""

import sys
import genCommon

_LIBGLX_FUNCTIONS = frozenset((
    "glXChooseVisual",
    "glXCopyContext",
    "glXCreateContext",
    "glXCreateGLXPixmap",
    "glXDestroyContext",
    "glXDestroyGLXPixmap",
    "glXGetConfig",
    "glXIsDirect",
    "glXMakeCurrent",
    "glXSwapBuffers",
    "glXUseXFont",
    "glXWaitGL",
    "glXWaitX",
    "glXQueryServerString",
    "glXGetClientString",
    "glXQueryExtensionsString",
    "glXChooseFBConfig",
    "glXCreateNewContext",
    "glXCreatePbuffer",
    "glXCreatePixmap",
    "glXCreateWindow",
    "glXDestroyPbuffer",
    "glXDestroyPixmap",
    "glXDestroyWindow",
    "glXGetFBConfigAttrib",
    "glXGetFBConfigs",
    "glXGetSelectedEvent",
    "glXGetVisualFromFBConfig",
    "glXMakeContextCurrent",
    "glXQueryContext",
    "glXQueryDrawable",
    "glXSelectEvent",
    "glXGetCurrentContext",
    "glXGetCurrentDrawable",
    "glXGetCurrentReadDrawable",
    "glXGetProcAddress",
    "glXGetProcAddressARB",
    "glXQueryExtension",
    "glXQueryVersion",
))

# These are functions to skip when we generate the entrypoint stubs. They
# require some additional typedefs that probably won't be available.
_SKIP_GLX_FUNCTIONS = frozenset((
    "glXAssociateDMPbufferSGIX",
    "glXCreateGLXVideoSourceSGIX",
    "glXDestroyGLXVideoSourceSGIX",
))

def generateGLXStubFunction(func):
    text = ""
    text += "typedef {f.rt} (*fn_{f.name}_ptr)({f.decArgs});\n"
    text += "static fn_{f.name}_ptr __real_{f.name};\n"
    if (func.name not in _LIBGLX_FUNCTIONS):
        text += "static glvnd_mutex_t __mutex_{f.name} = GLVND_MUTEX_INITIALIZER;\n"
    text += "PUBLIC {f.rt} {f.name}({f.decArgs})\n"
    text += "{{\n"
    text += "    fn_{f.name}_ptr _real = "
    if (func.name not in _LIBGLX_FUNCTIONS):
        text += "(fn_{f.name}_ptr) LOAD_GLX_FUNC({f.name});\n"
    else:
        text += "__real_{f.name};\n"

    text += "    if(_real != NULL) {{\n"
    if (func.hasReturn()):
        text += "        return _real({f.callArgs});\n"
        text += "    }} else {{\n"
        text += "        return {retVal};\n"
    else:
        text += "        _real({f.callArgs});\n"
    text += "    }}\n"
    text += "}}\n\n"

    return text.format(f=func, retVal=getDefaultReturnValue(func))

def generateLibGLXStubs(functions):
    text = r"""
/*
 * THIS FILE IS AUTOMATICALLY GENERATED BY gen_noop.pl
 * DO NOT EDIT!!
 */
#include <X11/Xlib.h>
#include <GL/glx.h>
#include "compiler.h"
#include "libgl.h"
#include "glvnd_pthread.h"

""".lstrip("\n")

    text += "#define LOAD_GLX_FUNC(name) __glXGLLoadGLXFunction(#name, (__GLXextFuncPtr *) &__real_##name, &__mutex_##name)\n\n"

    for func in functions:
        text += generateGLXStubFunction(func)

    text += "\n"
    text += "void __glXWrapperInit(void)\n"
    text += "{\n"
    for func in functions:
        if (func.name in _LIBGLX_FUNCTIONS):
            text += '    __glXGLLoadGLXFunction("{f.name}", (__GLXextFuncPtr *) &__real_{f.name}, NULL);\n'.format(f=func)
    text += "}\n"

    return text

def getDefaultReturnValue(func):
    POINTER_TYPE_NAMES = frozenset((
        "__GLXextFuncPtr",
        "GLXFBConfig", "GLXFBConfigSGIX",
        "GLXContext",
    ))
    XID_TYPE_NAMES = frozenset((
        "GLXContextID",
        "GLXWindow",
        "GLXPbuffer",
        "GLXPixmap",
        "GLXDrawable",
        "GLXFBConfigID",
        "GLXContextID",
        "GLXWindow",
        "GLXPbuffer",
        "GLXPbufferSGIX",
        "GLXVideoSourceSGIX",
    ))
    if (not func.hasReturn()):
        return ""

    if (func.rt.endswith("*")):
        return "NULL"

    if (func.rt in POINTER_TYPE_NAMES):
        return "NULL"

    if (func.rt in XID_TYPE_NAMES):
        return "None"

    if (func.rt == "Bool"):
        return "False"

    if (func.rt.startswith("GLX")):
        raise ValueError("Unknown GLX typedef: %r" % (func.rt,))

    return "0"

def _main():
    functions = genCommon.getFunctions(sys.argv[1:])
    functions = [f for f in functions if(f.name not in _SKIP_GLX_FUNCTIONS)]

    sys.stdout.write(generateLibGLXStubs(functions))

if (__name__ == "__main__"):
    _main()

