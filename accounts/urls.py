from django.urls import path
from accounts import views

app_name = 'accounts'
app_verbose_name = 'User Management'
urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
]
