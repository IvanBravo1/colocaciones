from django import forms
from .models import Empresa, Persona, Ofertas

class EmpresaForm(forms.ModelForm):
class PersonaForm(forms.ModelForm):
class OfertasForm(forms.ModelForm):

class Meta:
    model = Post
    fields = ('title', 'text',)
