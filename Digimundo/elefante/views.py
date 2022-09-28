from django.shortcuts import render, redirect
from .models import *
from .models import Post
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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

	context = { 'form' : form }
	return render(request, 'elefante/registro.html', context) 

@login_required
def retorno(request):
 
  return render(request, 'elefante/prueba.html')
 