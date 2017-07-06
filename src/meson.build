cc = meson.get_compiler('c')
libdl = cc.find_library('dl', required : false)
libm = cc.find_library('m')

# TODO: Handle these dynamically
c_defines = [
    'GLDISPATCH_USE_TLS',
    'HAVE_MINCORE',
    'HAVE_PTHREAD_RWLOCK_T',
    'HAVE_RTLD_NOLOAD',
    'HAVE_SYNC_INTRINSICS',
    'HAVE_TYPEOF',
    'USE_ATTRIBUTE_CONSTRUCTOR',
    'USE_X86_64_ASM',
]
foreach d : c_defines
  add_global_arguments('-D' + d + '=1', language : 'c')
endforeach

add_global_arguments('-fvisibility=hidden', language : 'c')
add_global_link_arguments('-Wl,-Bsymbolic', language : 'c')

subdir('generate')
subdir('util')
subdir('GLdispatch')
subdir('OpenGL')
subdir('EGL')
subdir('GLX')
subdir('GL')
subdir('GLESv1')
subdir('GLESv2')
