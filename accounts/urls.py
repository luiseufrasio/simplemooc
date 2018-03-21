from django.urls import path
from django.contrib.auth.views import (login, logout)

from . import views

app_name='accounts'
urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('entrar/', login, {'template_name': 'login.html'}, name='login'),
	path('sair/', logout, {'next_page': 'core:home'}, name='logout'),
	path('cadastre-se/', views.register, name='register'),
	path('nova-senha/', views.password_reset, name='password_reset'),
	path('confirmar-nova-senha/<slug:key>/', views.password_reset_confirm, name='password_reset_confirm'),
	path('editar/', views.edit, name='edit'),
	path('editar-senha/', views.edit_password, name='edit_password')
]