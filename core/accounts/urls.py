from django.urls import path
from core.accounts import views

app_name = 'core.accounts'
urlpatterns = [
    path('send_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
