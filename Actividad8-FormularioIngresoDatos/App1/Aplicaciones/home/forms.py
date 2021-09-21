from django import forms
from .models import Estudiantes

class EstudianteForm(forms.ModelForm):
    class meta:
        model = Estudiantes
        fields = '___all___'