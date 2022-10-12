from django.shortcuts import render
from django.http import HttpResponse

#acceso el sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')
   
def nosotros(request):
    return render(request,'paginas/nosotros.html')

      #acceso a libros

def libros(request):
    return render(request, "libros/index.html")    

def crear(request):
    return render(request, "libros/crear.html")

def Editar(request):
    return render(request, "libros/editar.html")    
