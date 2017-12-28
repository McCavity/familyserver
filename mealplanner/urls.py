from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealweek_list, name='mealweek_list'),
]
