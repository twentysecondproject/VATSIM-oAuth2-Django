from django.urls import path
from . import views


urlpatterns = [
    path('oauth2/login', views.vatsim_login, name='oauth_login'),
    path('oauth2/login/redirect', views.vatsim_login_redirect, name='vatsim_login_redirect'),
    path('logout/', views.logout, name='logout'),
]