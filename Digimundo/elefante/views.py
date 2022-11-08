from django.shortcuts import render, redirect
from .models import *
from .models import Post
from .models import Contacto
from .models import Carrito
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

#django nos permite tener forms#

# Create your views here.
# el context es para pedir datos a base


def feed(request):

    return render(request, 'elefante/feed.html')


def perfil(request):

    return render(request, 'elefante/perfil.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'elefante/registro.html', context)


@login_required
def retorno(request):

    return render(request, 'elefante/prueba.html')


def contactosregistro(request):
    if request.method == 'POST':

        datos = Post.objects.create(

            user_id=request.POST['user'],
            first_name=request.POST['nombre'],
            last_name=request.POST['apellidos'],
            telefono=request.POST['telefono'],
            telefono_casa=request.POST['telefono_casa'],
            nacimiento=request.POST['nacimiento'],
            direccion=request.POST['direccion'],
            contacto_emergencia=request.POST['contacto_emergencia'],
            telefono_emergencia=request.POST['telefono_emergencia'],
            puesto=request.POST['puesto'],
            departamento=request.POST['departamento'],
            is_leader=request.POST['is_leader'],

        )
        datos.save()
    return render(request, 'elefante/data.html')


def carru(request):

    return render(request, 'elefante/carru.html')


def mail(request):
    if request.method == 'POST':
        correoPrueba = request.POST['correo_electronico']
        asunto = request.POST['nombre_completo'] + ' ' + request.POST['username'] + ', ' + request.POST['celular'] + \
            ' con ' + request.POST['fecha_nacimiento'] + \
            ' con correo ' + request.POST['correo_electronico']
        correo = Contacto.objects.create(

            nombre_completo=request.POST['nombre_completo'],
            username=request.POST['username'],
            celular=request.POST['celular'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            direccion=request.POST['direccion'],
            correo_electronico=request.POST['correo_electronico'],


        )
        correo.save()

        send_mail(
            'Correo de Confirmacion',
            asunto,
            'Hola soy Andy y esto es una prueba ',
            [correoPrueba, 'andreamartinezdl1@gmail.com'],
            fail_silently=False
        )
    context = {}
    return render(request, 'elefante/mail.html')


def consultar(request):
    info = Post.objects.all()

    context = {'posts': info}

    #correo = Correo.objects.all()

    #context= {'datos': correo}
    return render(request, 'elefante/consulta.html', context)


def inicio(request):

    return render(request, 'elefante/inicio.html')


def carrito(request):
    print(str(request))
    if request.method == 'POST':

        carrito = Carrito.objects.create(

            nombre_completo=request.POST['nombre_completo'],
            celular=request.POST['celular'],
            direccion=request.POST['direccion'],
            correo_electronico=request.POST['correo_electronico'],
            total=request.POST['precioTotal'],
            user_id=request.POST['user']


        )
        carrito.save()

    return render(request, 'elefante/carrito.html')


def index(request):

    return render(request, 'elefante/index.html')
