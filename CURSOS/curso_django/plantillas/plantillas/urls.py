from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.hola, name='hola'),
    path('usuario/<str:name>/', views.dinamico, name='dinamico')
]
