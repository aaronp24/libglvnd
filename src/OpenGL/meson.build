# TODO: https://github.com/mesonbuild/meson/pull/1651 allows using
# g_opengl_exports_sym without .full_path(), but doesn't generate a dependency
# on src/generate/g_opengl_exports.sym for the link step.
opengl = shared_library('OpenGL', 'libopengl.c',
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
    include_directories : [inc, util_inc],
    version : '0.0.0',
    install : true,
)
