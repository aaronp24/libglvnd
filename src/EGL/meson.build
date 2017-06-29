egl = shared_library('EGL',
    [
        'libegl.c',
        'libeglcurrent.c',
        'libeglmapping.c',
        'libeglvendor.c',
        'libeglerror.c',
    ],
    c_args : [
         '-DDEFAULT_EGL_VENDOR_CONFIG_DIRS="@0@/glvnd/egl_vendor.d:@1@/glvnd/egl_vendor.d"'.format(
            sysconfdir, datadir),
    ],
    dependencies : [
        cJSON_dep,
        egl_dispatch_stubs_dep,
        gldispatch_dep,
        glvnd_pthread_dep,
        libdl,
        libm,
        utils_misc_dep,
        winsys_dispatch_dep,
    ],
    include_directories : [inc, util_inc],
    sources : g_egldispatchstubs_h,
    version : '1.0.0',
    install : true,
)
