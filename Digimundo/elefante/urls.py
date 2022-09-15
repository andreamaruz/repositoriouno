from django.urls import path
from . import views
urlpatterns = [
    path('', views.andrea, name='inicio')
]
