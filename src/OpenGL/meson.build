opengl_main_src = files('libopengl.c')
opengl_main_inc = [inc, util_inc, gldispatch_inc]

opengl = shared_library('OpenGL', opengl_main_src,
    link_depends : [
        g_opengl_exports_sym,
    ],
    link_whole : [
        glapi_opengl,
    ],
    dependencies : [
        gldispatch_dep,
        g_opengl_exports_sym_dep,
    ],
    include_directories : opengl_main_inc,
    version : '0.0.0',
    install : true,
)
