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
