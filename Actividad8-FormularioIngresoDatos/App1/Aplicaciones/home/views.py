from .models import Administradores, Estudiantes
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .forms import EstudianteForm
from django.urls import reverse_lazy


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

class ListarEstudiante(ListView):
    template_name = 'Estudiantes.html'
    model = Estudiantes

    def get_queryset(self):
        return Estudiantes.objects.all()

class ListarAdmins(ListView):
    template_name='Administradores.html'

    def get_queryset(self):
        return Administradores.objects.all()


class CrearEstudianteView(CreateView):
    template_name = 'crear.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('Aplicaciones:home') 