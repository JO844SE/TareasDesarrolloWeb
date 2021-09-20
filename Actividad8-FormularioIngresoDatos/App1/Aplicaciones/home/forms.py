from django import forms
from .models import Administradores

class EstudianteForm(forms.ModelForm):
    class meta:
        model = Administradores
        fields = '___all___'