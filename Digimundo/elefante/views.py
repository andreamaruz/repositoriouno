from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def andrea(request):
    template ='elefante/prueba.html'
    user = User.objects.all()

    context={'user': user}
    return render(request, template,context)