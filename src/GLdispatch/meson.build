subdir('vnd-glapi')

gldispatch_inc = include_directories([
    'vnd-glapi',
    '.',
])

# TODO: soname
gldispatch = shared_library('GLdispatch', 'GLdispatch.c',
    include_directories : [inc, util_inc, gldispatch_inc],
    link_whole : [
        glapi,
    ],
    dependencies : [
        glvnd_pthread_dep,
        app_error_check_dep,
        libdl,
    ],
    version : '0.0.0',
    install : true,
)
gldispatch_dep = declare_dependency(
    link_with : gldispatch,
    include_directories : gldispatch_inc,
)
