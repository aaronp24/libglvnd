project('libglvnd', 'c', meson_version : '>=0.41')

glproto_dep = dependency('glproto', required : true)
x11_dep = dependency('x11', required : true)
xext_dep = dependency('xext', required : true)

inc = include_directories('include')

datadir = join_paths(get_option('prefix'), get_option('datadir'))
sysconfdir = join_paths(get_option('prefix'), get_option('sysconfdir'))

subdir('src')
subdir('include')
subdir('tests')

import('pkgconfig').generate(
    name : 'libglvnd',
    version : '1.0.0',
    description : 'Vendor-neutral OpenGL dispatch library vendor interface',
    variables : [
        'datarootdir=${prefix}/@0@'.format(datadir),
        'datadir=${datarootdir}',
    ],
)
