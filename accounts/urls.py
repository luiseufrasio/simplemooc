from django.urls import path
from django.contrib.auth.views import (login, logout)

from . import views

app_name='accounts'
urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('entrar/', login, {'template_name': 'login.html'}, name='login'),
	path('cadastre-se/', views.register, name='register'),
	path('sair/', logout, {'next_page': 'core:home'}, name='logout')
]