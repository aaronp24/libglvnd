cc = meson.get_compiler('c')
libdl = cc.find_library('dl', required : false)
libm = cc.find_library('m')

# TODO: Handle these dynamically
c_defines = [
    'HAVE_MINCORE',
    'HAVE_PTHREAD_RWLOCK_T',
    'HAVE_RTLD_NOLOAD',
    'HAVE_SYNC_INTRINSICS',
    'HAVE_TYPEOF',
    'USE_ATTRIBUTE_CONSTRUCTOR',
]

if get_option('asm')
  if host_machine.cpu_family() == 'x86'
    c_defines += ['USE_X86_ASM', 'USE_MMX_ASM', 'USE_3DNOW_ASM', 'USE_SSE_ASM']
  elif host_machine.cpu_family() == 'x86_64'
    c_defines += ['USE_X86_64_ASM']
  elif host_machine.cpu_family() == 'armv7l'
    c_defines += ['USE_ARMV7_ASM']
  elif host_machine.cpu_family() == 'aarch64'
    c_defines += ['USE_AARCH64_ASM']
  elif host_machine.cpu_family() == 'ppc64le'
    c_defines += ['USE_PPC64LE_ASM']
  endif
endif

if get_option('tls')
  use_tls = cc.compiles('__thread int foo __attribute__((tls_model("initial-exec")));', name : 'TLS detection')
else
  use_tls = false
endif

if ['x86', 'x86_64'].contains(host_machine.cpu_family())
  if use_tls
    c_defines += ['GLDISPATCH_USE_TLS']
    dispatch_entry_type = '@0@_tls'.format(host_machine.cpu_family())
  else
    dispatch_entry_type = '@0@_tsd'.format(host_machine.cpu_family())
  endif
elif host_machine.cpu_family() == 'armv7l'
  dispatch_entry_type = 'armv7_tsd'
elif host_machine.cpu_family() == 'aarch64'
  dispatch_entry_type = 'aarch64_tsd'
elif host_machine.cpu_family() == 'ppc64le'
  if use_tls
    c_defines += ['GLDISPATCH_USE_TLS']
    dispatch_entry_type = 'ppc64le_tls'
  else
    dispatch_entry_type = 'ppc64le_tsd'
  endif
else
  # The C stubs will work with either TLS or TSD.
  gldispatch_entry_type = 'pure_c'
endif

foreach d : c_defines
  add_project_arguments('-D' + d + '=1', language : 'c')
endforeach

add_project_arguments('-fvisibility=hidden', language : 'c')
add_project_link_arguments('-Wl,-Bsymbolic', language : 'c')

subdir('generate')
subdir('util')
subdir('GLdispatch')
subdir('OpenGL')

if get_option('egl')
  subdir('EGL')
endif

if get_option('glx')
  subdir('GLX')
  subdir('GL')
endif

if get_option('gles')
  subdir('GLESv1')
  subdir('GLESv2')
endif
