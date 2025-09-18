from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'aboutme.html', {})

def projects(request):
    return render(request, 'projects.html', {})