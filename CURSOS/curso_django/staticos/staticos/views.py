from django.shortcuts import render

def estatico(request):
    return render(request, 'index.html', {})