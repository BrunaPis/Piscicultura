from django.shortcuts import render, redirect
from django.contrib import admin
#from app.form import PiscicultoresForm, PeixesForm
#from app.form import ViveirosForm2, RacaoForm
#from app.models import Piscicultores, Viveiros, Peixes, Racao
#from django.contrib.auth.views import LoginView, LogoutView
#from django.urls import reverse_lazy
#from django.core.paginator import Paginator
#from django.shortcuts import  HttpResponse



def login(request):
    return render(request,'login.html')

def Index(request):
    return render(request, 'Index.html')

def home(request):
    return render(request, 'home.html')

def create_piscicultor(request):
    return render(request, 'create_piscicultor.html')

def create_viveiro(request):
    return render(request, 'create_viveiro.html')

def create_peixe(request):
    return render(request, 'create_peixe.html')

def create_racao(request):
    return render(request, 'create_racao.html')