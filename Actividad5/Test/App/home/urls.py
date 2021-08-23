"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from App.home.views import AdminView, CreditosView, EstudiantesView, HomeView, InfoView, ViewHom

app_name='app1'

urlpatterns = [
    path('index/', ViewHom.as_view(), name='index'),
    path('bienvenida/', HomeView.as_view(), name='home'),
    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),
    path('administradores/', AdminView.as_view(), name='administradores'),
    path('informacion/', InfoView.as_view(), name='info'),
    path('creditos/', CreditosView.as_view(), name='creditos'),
]
