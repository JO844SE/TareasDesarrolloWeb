from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'


class CreditosView(TemplateView):
    template_name='creditos.html'
    

class EstudiantesView(TemplateView):
    template_name='Estudiantes.html'


class AdministradoresView(TemplateView):
    template_name='Administradores.html'


class AcercaDeView(TemplateView):
    template_name='Acerca.html'