from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido Develoteca<h1>")

def nosotros(request):
    return render(request,'paginas/nosotros.html')

# Create your views here.
