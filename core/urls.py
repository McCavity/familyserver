from django.urls import path
from . import views

urlpatterns = [
    path('core/', views.home_page, name='home'),
]
