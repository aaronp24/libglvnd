glx_inc = include_directories('.')

glx_src = [
    'libglx.c',
    'libglxmapping.c',
    'libglxproto.c',
]

glx = shared_library('GLX',
    sources : glx_src,
    include_directories: [inc, util_inc],
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

glx_dep = declare_dependency(link_with : glx)
