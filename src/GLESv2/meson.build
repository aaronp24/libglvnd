glesv2 = shared_library('GLESv2', opengl_main_src,
    include_directories : opengl_main_inc,
    link_whole : [
        glapi_glesv2,
    ],
    dependencies : [
        gldispatch_dep,
    ],
    version : '2.1.0',
    install : true,
)
