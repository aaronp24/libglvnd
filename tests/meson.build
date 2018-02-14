subdir('dummy')

# The entrypoint patching tests need --smc-check=full when running under
# Valgrind.
add_test_setup('valgrind',
    exe_wrapper : [
        'valgrind', '--error-exitcode=1', '--leak-check=full', '--smc-check=all',
    ],
    timeout_multiplier : 100
)

env = ['LD_LIBRARY_PATH=@0@/dummy'.format(meson.current_build_dir())]
glx_env = env + ['__GLX_VENDOR_LIBRARY_NAME=dummy']
glx_genentry = env + ['__GLX_FORCE_VENDOR_LIBRARY_0=dummy']
glx_patch = glx_env + ['GLVND_TEST_PATCH_ENTRYPOINTS=1']
glx_threads = glx_env + ['LD_PRELOAD=libpthread.so.0']
egl_env = env + ['__EGL_VENDOR_LIBRARY_DIRS=@0@/json'.format(meson.current_source_dir())]

gldispatch = executable('testgldispatch', 'testgldispatch.c',
    include_directories : [inc, gldispatch_inc],
    link_with : [opengl, gldispatch, libpatchentrypoints],
)

glxcreatecontext_src = files('testglxcreatecontext.c', 'test_utils.c')
glxcreatecontext = executable('testglxcreatecontext', glxcreatecontext_src,
    include_directories : inc,
    dependencies : [x11_dep, glvnd_pthread_dep, libdl],
    link_with : [glx, opengl],
)

glxmakecurrent_src = files('testglxmakecurrent.c', 'test_utils.c')
glxmakecurrent = executable('testglxmakecurrent', glxmakecurrent_src,
    include_directories : inc,
    dependencies : [x11_dep, glvnd_pthread_dep, libdl],
    link_with : [glx, opengl],
)

glxmakecurrent_oldlink = executable('testglxmakecurrent_oldlink', glxmakecurrent_src,
    include_directories : inc,
    dependencies : [x11_dep, glvnd_pthread_dep, libdl],
    link_with : gl,
)

glxgetprocaddress = executable('testglxgetprocaddress', 'testglxgetprocaddress.c',
    include_directories : inc,
    dependencies : x11_dep,
    link_with : glx,
)

glxgetclientstr = executable('testglxgetclientstr', 'testglxgetclientstr.c',
    include_directories : inc,
    dependencies : x11_dep,
    link_with : glx,
)

glxqueryversion = executable('testglxqueryversion', 'testglxqueryversion.c',
    include_directories : inc,
    dependencies : x11_dep,
    link_with : glx,
)

patchentrypoints = executable('patchentrypoints',
    ['testpatchentrypoints.c', 'test_utils.c'],
    include_directories : inc,
    dependencies : [x11_dep, libdl],
    link_with: [glx, opengl],
)

if get_option('egl')
  egl_test_utils = static_library('egl_test_utils', 'egl_test_utils.c',
      include_directories : inc,
  )

  egldisplay = executable('testegldisplay', 'testegldisplay.c',
      include_directories : inc,
      dependencies : x11_dep,
      link_with : [egl, egl_test_utils],
  )

  egldevice = executable('testegldevice', 'testegldevice.c',
      include_directories : inc,
      dependencies : x11_dep,
      link_with : [egl, egl_test_utils],
  )

  eglgetprocaddress = executable('testeglgetprocaddress', 'testeglgetprocaddress.c',
      include_directories : inc,
      dependencies : x11_dep,
      link_with : [egl, egl_test_utils],
  )

  eglmakecurrent = executable('testeglmakecurrent', 'testeglmakecurrent.c',
      include_directories : [inc, util_inc],
      dependencies : x11_dep,
      link_with : [egl, opengl, egl_test_utils],
  )

  eglerror = executable('testeglerror', 'testeglerror.c',
      include_directories : inc,
      dependencies : x11_dep,
      link_with : [egl, egl_test_utils],
  )

  egldebug = executable('testegldebug', 'testegldebug.c',
      include_directories : inc,
      dependencies : x11_dep,
      link_with : [egl, egl_test_utils],
  )
endif

test('gldispatch_static',          gldispatch,               args : ['-s'],                        env : env)
test('gldispatch_generated',       gldispatch,               args : ['-g'],                        env : env)
test('gldispatch_patched',         gldispatch,               args : ['-s', '-g', '-p'],            env : env)
test('glxcreatecontext',           glxcreatecontext,                                               env : glx_env)
test('glxmcbasic',                 glxmakecurrent,           args : ['-t', '1', '-i', '1'],        env : glx_env)
test('glxmcloop',                  glxmakecurrent,           args : ['-t', '1', '-i', '250'],      env : glx_env)
test('glxmcthreads',               glxmakecurrent,           args : ['-t', '5', '-i', '20000'],    env : glx_threads)
test('glxmclate',                  glxmakecurrent,           args : ['-t', '1', '-i', '1', '-l'],  env : glx_env)
test('glxmcoldlink',               glxmakecurrent_oldlink,   args : ['-t', '1', '-i', '1'],        env : glx_env)
test('glxgetprocaddress',          glxgetprocaddress,                                              env : glx_env)
test('glxgetprocaddress_genentry', glxgetprocaddress,                                              env : glx_genentry)
test('glxgetclientstr',            glxgetclientstr,                                                env : glx_env)
test('glxqueryversion',            glxqueryversion,                                                env : glx_env)
test('patchentrypoints',           patchentrypoints,                                               env : glx_patch)

if get_option('egl')
  test('egldisplay',                 egldisplay,                                                     env : egl_env)
  test('egldevice',                  egldevice,                                                      env : egl_env)
  test('eglgetprocaddress',          eglgetprocaddress,                                              env : egl_env)
  test('eglmakecurrent',             eglmakecurrent,                                                 env : egl_env)
  test('eglerror',                   eglerror,                                                       env : egl_env)
  test('egldebug',                   egldebug,                                                       env : egl_env)
endif
