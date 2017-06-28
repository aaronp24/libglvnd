gen_mapi_script = find_program('gen_gldispatch_mapi.py')
glapi_gen_gl_core_xml = files('xml/gl.xml')
glapi_gen_gl_xml = glapi_gen_gl_core_xml + files('xml/gl_other.xml')

glapi_mapi_gen = custom_target('glapi_mapi_tmp.h',
    command : [gen_mapi_script, 'gldispatch', glapi_gen_gl_xml],
    capture : true,
    depend_files : files('genCommon.py') + glapi_gen_gl_xml,
    output : 'glapi_mapi_tmp.h',
)
glapi_mapi_dep = declare_dependency(
    sources : glapi_mapi_gen,
)

# opengl
glapi_mapi_opengl_gen = custom_target('glapi_mapi_opengl_tmp.h',
    command : [gen_mapi_script, 'opengl', glapi_gen_gl_xml],
    capture : true,
    depend_files : files('genCommon.py') + glapi_gen_gl_xml,
    output : 'glapi_mapi_opengl_tmp.h',
)
glapi_mapi_opengl_dep = declare_dependency(
    sources : glapi_mapi_opengl_gen,
)

# gl
glapi_mapi_gl_gen = custom_target('glapi_mapi_gl_tmp.h',
    command : [gen_mapi_script, 'gl', glapi_gen_gl_xml],
    capture : true,
    depend_files : files('genCommon.py') + glapi_gen_gl_xml,
    output : 'glapi_mapi_gl_tmp.h',
)
glapi_mapi_gl_dep = declare_dependency(
    sources : glapi_mapi_gl_gen,
)

glapi_gen_libglglxstubs_script = find_program('gen_libgl_glxstubs.py')
glapi_gen_glx_xml = files('xml/glx.xml', 'xml/glx_other.xml')
libglglxwrapper_gen = custom_target('g_libglglxwrapper.c',
    command : [glapi_gen_libglglxstubs_script, glapi_gen_glx_xml],
    capture : true,
    depend_files : files('genCommon.py') + glapi_gen_glx_xml,
    output : 'g_libglglxwrapper.c',
)
libglglxwrapper_dep = declare_dependency(
    sources : libglglxwrapper_gen,
)

glapi_gen_libopengl_exports_script = find_program('gen_libOpenGL_exports.py')
g_opengl_exports_sym = custom_target('g_opengl_exports.sym',
    command : [glapi_gen_libopengl_exports_script, 'opengl', glapi_gen_gl_core_xml],
    capture : true,
    depend_files : files('genCommon.py', 'gen_libOpenGL_exports.py') + glapi_gen_gl_core_xml,
    output : 'g_opengl_exports.sym',
)
g_opengl_exports_sym_dep = declare_dependency(
    sources : g_opengl_exports_sym,
    link_args : '-Wl,--version-script,@0@'.format(g_opengl_exports_sym.full_path()),
)

# EGL_dispatch_stubs
# TODO: Move egldispatchstubs.h to here
egl_inc = include_directories('../EGL')
egl_gen_dispatch_script = find_program('gen_egl_dispatch.py')
egl_gen_files = files('eglFunctionList.py', 'xml/egl.xml')
g_egldispatchstubs_c = custom_target('g_egldispatchstubs.c',
    command : [egl_gen_dispatch_script, 'source', egl_gen_files],
    capture : true,
    depend_files : files('gen_egl_dispatch.py') + egl_gen_files,
    output : 'g_egldispatchstubs.c',
)
g_egldispatchstubs_h = custom_target('g_egldispatchstubs.h',
    command : [egl_gen_dispatch_script, 'header', egl_gen_files],
    capture : true,
    depend_files : files('gen_egl_dispatch.py') + egl_gen_files,
    output : 'g_egldispatchstubs.h',
)
egl_dispatch_stubs_inc = include_directories(meson.current_build_dir())
egl_dispatch_stubs = static_library('EGL_dispatch_stubs',
    [
        '../EGL/egldispatchstubs.c',
        g_egldispatchstubs_c,
    ],
    include_directories : [inc, egl_inc, egl_dispatch_stubs_inc],
    sources : g_egldispatchstubs_h,
)
egl_dispatch_stubs_dep = declare_dependency(link_with : egl_dispatch_stubs,
    depend_files : g_egldispatchstubs_h)
