libpatchentrypoints = static_library('patchentrypoints.a', 'patchentrypoints.c',
    include_directories : [inc, util_inc],
)

if get_option('glx')
  glx_dummy = shared_library('GLX_dummy', 'GLX_dummy.c',
      include_directories : [inc, util_inc],
      dependencies : x11_dep,
      link_with : libpatchentrypoints,
      version : '0',
  )
endif

if get_option('egl')
  egl_dummy0 = shared_library('EGL_dummy0', 'EGL_dummy.c',
      include_directories : [inc, util_inc],
      c_args : '-D DUMMY_VENDOR_NAME="dummy0"',
      dependencies : [x11_dep, glvnd_pthread_dep, libdl],
      link_with : libpatchentrypoints,
      version : '0',
  )

  egl_dummy1 = shared_library('EGL_dummy1', 'EGL_dummy.c',
      include_directories : [inc, util_inc],
      c_args : '-D DUMMY_VENDOR_NAME="dummy1"',
      dependencies : [x11_dep, glvnd_pthread_dep, libdl],
      link_with : libpatchentrypoints,
      version : '0',
  )
endif
