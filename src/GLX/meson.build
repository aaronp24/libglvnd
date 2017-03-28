glx_inc = include_directories('.')

glx_src = [
    'libglx.c',
    'libglxmapping.c',
    'libglxproto.c',
]

# TODO: Should these be in a config.h?
glx_c_args = [
    '-DHAVE_SYNC_INTRINSICS',
    '-DUSE_X86_64_ASM',
]

glx = shared_library('GLX',
    sources : glx_src,
    include_directories: [inc, util_inc],
    c_args : glx_c_args,
    dependencies : [
        gldispatch_dep,
        glvnd_genentry_dep,
        glvnd_pthread_dep,
        winsys_dispatch_dep,
        libdl,
        dependency('glproto'),
        dependency('x11'),
        dependency('xext'),
    ],
    version : '0.0.0',
    install : true,
)
