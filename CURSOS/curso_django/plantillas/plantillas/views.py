from django.shortcuts import render

def hola(request):
    return render(request, 'index.html', {})

def dinamico(request, name):
    context = {'name' : name}
    return render(request, 'dinamico.html', context)