glesv1_cm = shared_library('GLESv1_CM', opengl_main_src,
    include_directories : opengl_main_inc,
    link_depends : [
        g_glesv1_exports_sym,
    ],
    link_whole : [
        glapi_glesv1,
    ],
    dependencies : [
        gldispatch_dep,
        g_glesv1_exports_sym_dep,
    ],
    version : '1.2.0',
    install : true,
)
