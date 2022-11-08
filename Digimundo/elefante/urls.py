from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.feed, name='feed'),
    url('^perfil/$', views.perfil, name="perfil"),
    url('^register/$', views.registro, name="registro"),
    url('^login/$', LoginView.as_view(template_name='elefante/login.html'), name="login"),
    url('^logout/$', LogoutView.as_view(template_name='elefante/logout.html'), name="logout"),
    url('^acceso/$', views.retorno, name="prueba"),
    url('^data/$', views.contactosregistro, name="contactosregistro"),
    url('^carousel/$', views.carru, name="carousel"),
    url('^mail/$', views.mail, name="mail"),
    url('^consulta/$', views.consultar, name="consulta"),
    url('^inicio/$', views.inicio, name="inicio"),
    url('^feed/$', views.feed, name="feed"),
    url('^carrito/$', views.carrito, name="carrito"),
    url('^index/$', views.index, name="index"),

]
