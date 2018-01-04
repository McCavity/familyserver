from django import template

register = template.Library()

''' returns verbose_name attribute of the `app_name` app '''
@register.simple_tag
def get_app_verbose_name(app_name):
    from django.conf import settings
    from importlib import import_module 
    full_name = ''
    for app in settings.INSTALLED_APPS:
        if app_name.lower() == app.split('.')[-1]:
            full_name = app
            break
    verbose_name = ''
    if full_name != '':
        module = import_module(full_name) 
        verbose_name = getattr(module, 'verbose_name', None) or app_name
    if verbose_name != '':
        return verbose_name
    return 'No App Name Set'
