from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ViewHom(TemplateView):
    template_name = 'index.html'


class EstudiantesView(TemplateView):
    template_name = 'estudiantes.html'



class AdminView(TemplateView):
    template_name = 'administradores.html'


class CreditosView(TemplateView):
    template_name = 'creditos.html'

class InfoView(TemplateView):
    template_name = 'info.html'



