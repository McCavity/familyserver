from django.urls import path
from . import views

app_name = 'mealplanner'
urlpatterns = [
    path('', views.mealweek_list, name='mealweek_list'),
    path('mealweek/<int:pk>', views.mealweek_detail, name='mealweek_detail'),
]
