from django.shortcuts import render

# Create your views here.

def crear(request): 
    return render(request,'app/crear.html')

def leer(request): 
    return render(request,'app/leer.html')

def update(request): 
    return render(request,'app/update.html') 