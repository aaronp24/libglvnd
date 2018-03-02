entry_src = []

pre_glapi_src = []

if dispatch_entry_type == 'x86_tls'
  entry_src += ['entry_x86_tls.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'x86_tsd'
  entry_src += ['entry_x86_tsd.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'x86_64_tls'
  entry_src += ['entry_x86_64_tls.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'x86_64_tsd'
  entry_src += ['entry_x86_64_tsd.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'armv7_tsd'
  entry_src += ['entry_armv7_tsd.c', 'entry_common.c']
elif dispatch_entry_type == 'aarch64_tsd'
  entry_src += ['entry_aarch64_tsd.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'ppc64le_tls'
  entry_src += ['entry_ppc64le_tls.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'ppc64le_tsd'
  entry_src += ['entry_ppc64le_tsd.c', 'entry_simple_asm.c', 'entry_common.c']
elif dispatch_entry_type == 'pure_c'
  entry_src += 'entry_pure_c.c'
endif

if use_tls
  pre_glapi_src += 'u_current_tls.c'
else
  pre_glapi_src += 'u_current_tsd.c'
endif

glapi_src = entry_src + pre_glapi_src + [
    'mapi_glapi.c',
    'stub.c',
    'table.c',
    'u_execmem.c',
]

glapi = static_library('glapi',
    sources : glapi_src,
    include_directories : [inc, util_inc],
    c_args : '-DMAPI_ABI_HEADER="glapi_mapi_tmp.h"',
    dependencies : [
        glapi_mapi_dep,
        utils_misc_dep,
    ],
)

glapi_gl = static_library('glapi_gl',
    sources : [entry_src, 'stub.c'],
    include_directories : [inc, util_inc],
    c_args : [
        '-DMAPI_ABI_HEADER="glapi_mapi_gl_tmp.h"',
        '-DSTATIC_DISPATCH_ONLY',
    ],
    dependencies : [
        glapi_mapi_gl_dep,
        utils_misc_dep,
    ],
)

glapi_opengl = static_library('glapi_opengl',
    sources : [entry_src, 'stub.c'],
    include_directories : [inc, util_inc],
    c_args : [
        '-DMAPI_ABI_HEADER="glapi_mapi_opengl_tmp.h"',
        '-DSTATIC_DISPATCH_ONLY',
    ],
    dependencies : [
        glapi_mapi_opengl_dep,
        utils_misc_dep,
    ],
)

# TODO: Abstract STATIC_DISPATCH_ONLY
glapi_glesv1 = static_library('glapi_glesv1',
    sources : [entry_src, 'stub.c'],
    include_directories : [inc, util_inc],
    c_args : [
        '-DMAPI_ABI_HEADER="glapi_mapi_glesv1_tmp.h"',
        '-DSTATIC_DISPATCH_ONLY',
    ],
    dependencies : [
        glapi_mapi_glesv1_dep,
        utils_misc_dep,
    ],
)

glapi_glesv2 = static_library('glapi_glesv2',
    sources : [entry_src, 'stub.c'],
    include_directories : [inc, util_inc],
    c_args : [
        '-DMAPI_ABI_HEADER="glapi_mapi_glesv2_tmp.h"',
        '-DSTATIC_DISPATCH_ONLY',
    ],
    dependencies : [
        glapi_mapi_glesv2_dep,
        utils_misc_dep,
    ],
)
