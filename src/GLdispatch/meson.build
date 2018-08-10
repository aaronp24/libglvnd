subdir('vnd-glapi')

gldispatch_inc = include_directories([
    'vnd-glapi',
    '.',
])

if use_tls
  gldispatch_linker_script = 'export_list_tls.ver'
else
  gldispatch_linker_script = 'export_list_tsd.ver'
endif

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
    link_depends : gldispatch_linker_script,
    version : '0.0.0',
    install : true,
    link_args : '-Wl,--version-script,@0@/@1@'.format(meson.current_source_dir(), gldispatch_linker_script),
)
gldispatch_dep = declare_dependency(
    link_with : gldispatch,
    include_directories : gldispatch_inc,
)
