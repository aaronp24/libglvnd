cc =meson.get_compiler('c')
libdl = cc.find_library('libdl')

add_global_arguments('-DUSE_ATTRIBUTE_CONSTRUCTOR', language : 'c')

subdir('generate')
subdir('util')
subdir('GLdispatch')
subdir('OpenGL')
subdir('EGL')
subdir('GLX')
subdir('GL')
subdir('GLESv1')
subdir('GLESv2')
