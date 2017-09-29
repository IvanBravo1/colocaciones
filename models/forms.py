from django import forms
from .models import Empresa, Desocupado, Ofertas

class EmpresaForm(forms.ModelForm):
class DesocupadoForm(forms.ModelForm):
class OfertasForm(forms.ModelForm):

class Meta:
    model = Post
    fields = ('title', 'text',)
