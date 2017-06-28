project('libglvnd', 'c')

inc = include_directories('include')

datadir = join_paths(get_option('prefix'), get_option('datadir'))
sysconfdir = join_paths(get_option('prefix'), get_option('sysconfdir'))

subdir('src')
subdir('include')

import('pkgconfig').generate(
    name : 'libglvnd',
    version : '0.2.999',
    description : 'Vendor-neutral OpenGL dispatch library vendor interface',
    variables : [
        'datarootdir=${prefix}/@0@'.format(datadir),
        'datadir=${datarootdir}',
    ],
)
