from django.shortcuts import render
import random

from django.urls.conf import path

def home(request):
    return render(request,'ejercicio/home.html',{'nombre':'yahir torres'})

def nueva(request):
    return render(request, 'ejercicio/nuevapagina.html')

def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('@#$%^&*()'))
    lenght = int(request.GET.get('lenght',8))
    pswd = ''
    for x in range(lenght):
        pswd += random.choice(caracteres)
    return render(request,'ejercicio/password.html',{'password':pswd})