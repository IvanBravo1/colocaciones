from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from app.core.forms import *

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})

def ofertas(request):
    ofertas = Oferta.objects.all().filter(empresa = request.user.empresa)
    return render(request, 'home.html', {'ofertas': ofertas})

def oferta_nueva(request):
    if request.method == "POST":
        form = OfertaForm(request.POST)
        if form.is_valid():
            job = form.save(commit = False)
            job.empresa = request.user.empresa
            job.save()
            return redirect('home')
    else:
        form = OfertaForm()
        return render(request, 'editar_oferta.html', {'form': form})

def editar_oferta(request, pk):
    oferta = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            oferta = form.save
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
    return HttpResponseRedirect('/home')

def eliminar_usuario(request, user_id):
	User.objects.get(id=user_id).delete()
	return render(request, 'eliminar_usuario.html', {'id': user_id})

@login_required
def editar(request):
    user = User.objects.get(id=request.user.id)
    if user.is_desocupado():
        form = EditarDesocupado
        data = user.desocupado
    elif user.is_Empresa():
        form = EditarEmpresa
        data = user.empresa
    if request.method == "GET":
        return get_editar_form(request, form, data)
    elif request.method == 'POST':
        return handle_editar_form(request, form,data)

def get_editar_form(request,formName, data):
    form = formName(instance=data)
    return render(request, 'signup.html', {'form':form})

def handle_editar_form(request,formName, data):
    form = formName(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'signup.html', {'form':form})


# Las de abajo son las vistas que ya tenían, fijense cuales sirven y cuales
# quedan ya obsoletas con las de arriba.
"""
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

"""
