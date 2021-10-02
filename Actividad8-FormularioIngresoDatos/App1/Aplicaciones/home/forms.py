from django import forms
from django.forms import fields
from .models import Administradores, Estudiantes


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'

class AdministradoresForm(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'