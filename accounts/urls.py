from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name='accounts'
urlpatterns = [
	path('entrar/', login, {'template_name': 'login.html'}, name='login'),
	path('cadastre-se/', views.register, name='register'),
]