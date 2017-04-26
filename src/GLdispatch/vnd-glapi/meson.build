entry_src = [
    'entry_x86_64_tls.c',
    'entry_x86_64_common.c',
    'entry_common.c',
]

glapi_src = entry_src + [
    'mapi_glapi.c',
    'stub.c',
    'table.c',
    'u_execmem.c',
    'u_current_tls.c',
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
