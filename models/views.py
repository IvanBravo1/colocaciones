from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from .models import Empresa
from .models import Desocupado
from .models import Oferta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import Group, User

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/eleccion')
    else:
        formulario = UserCreationForm()
    return render(request, 'nuevo_usuario.html', {'formulario':formulario})

def nuevo_usuario_empresa(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/ingresar')
    else:
        formulario = UserCreationForm()
    return render(request, 'reg_empresa.html', {'formulario':formulario})

def nuevo_usuario_desocupado(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/ingresar')
    else:
        formulario = UserCreationForm()
    return render(request, 'reg_desocupado.html', {'formulario':formulario})

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/inicio')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/inicio')
                else:
                    return render(request, 'noactivo.html', context=None)
            else:
                return render(request, 'nousuario.html', context=None)
    else:
        formulario = AuthenticationForm()

    return render(request, 'ingresar.html', {'formulario':formulario})

def eleccion(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request, 'eleccion.html', {'formulario':formulario})

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def inicio(request):
    oferta = Oferta.objects.all().order_by('created_date')
    grupo = Group.objects.get(name="Empresa").user_set.all()
    return render(request, 'inicio.html', {'oferta': oferta, 'grupo':grupo})

def crear_oferta(request):
    if request.method == "POST":
        form = OfertaForm(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.author = request.user
            oferta.published_date = timezone.now()
            oferta.save()
            return HttpResponseRedirect('/inicio')
    else:
        form = OfertaForm()
        return render(request, 'editar_oferta.html', {'form': form})

def editar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method == "POST":
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.author = request.user
            oferta.save()
            return HttpResponseRedirect('/')
    else:
        form = OfertaForm(instance=oferta)
    if request.user == oferta.author:
        return render(request, 'editar_oferta.html', {'form': form})
    else:
        return render(request, 'oferta_completa.html', {'oferta': oferta})

def eliminar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    oferta.delete()
    return HttpResponseRedirect('/inicio')

def oferta_usuario(request, pk):
    usr = get_object_or_404(User, pk=pk)
    oferta = Oferta.objects.filter(author=usr)
    return render(request, 'oferta_usuario.html', {'oferta': oferta, 'usuario':usr})

def oferta_completa(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    return render(request, 'oferta_completa.html', {'oferta': oferta})


