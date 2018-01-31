gl = shared_library('GL',
    [
        'libgl.c',
        libglglxwrapper_gen,
    ],
    link_whole : [
        glapi_gl,
    ],
    dependencies : [
        glx_dep,
        gldispatch_dep,
        x11_dep,
    ],
    include_directories : [inc, glx_inc, util_inc],
    version : '1.7.0',
    install : true,
)
