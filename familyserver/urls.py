"""familyserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from core import views as core_views
from accounts import urls as accounts_urls
from core import urls as core_urls
from lists import views as lists_views
from lists import urls as lists_urls
from mealplanner import views as mealplanner_views
from mealplanner import urls as mealplanner_urls

urlpatterns = [
    #path('', core.views.home_page, name='core'),
    path('', include(core_urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=False), name='favicon'),
    path('accounts/', include(accounts_urls)),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('lists/', include(lists_urls)),
    path('mealplanner/', include(mealplanner_urls)),
]
