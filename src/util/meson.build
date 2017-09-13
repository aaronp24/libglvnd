util_inc = include_directories('.', 'uthash/src')

app_error_check = static_library('libapp_error_check', 'app_error_check.c',
    include_directories: inc,
)
app_error_check_dep = declare_dependency(
    link_with : app_error_check,
    include_directories : util_inc,
)

cJSON = static_library('cJSON', 'cJSON.c')
cJSON_dep = declare_dependency(
    link_with : cJSON,
)

glvnd_genentry = static_library('libglvnd_genentry', 'glvnd_genentry.c')
glvnd_genentry_dep = declare_dependency(
    link_with : glvnd_genentry,
)

glvnd_pthread = static_library('libglvnd_pthread', 'glvnd_pthread.c')
glvnd_pthread_dep = declare_dependency(
    link_with : glvnd_pthread,
    include_directories : util_inc,
)

utils_misc = static_library('libutils_misc', 'utils_misc.c')
utils_misc_dep = declare_dependency(
    link_with : utils_misc,
)

winsys_dispatch = static_library('libwinsys_dispatch', 'winsys_dispatch.c',
    include_directories : [inc, util_inc],
)
winsys_dispatch_dep = declare_dependency(
    link_with : winsys_dispatch,
)
