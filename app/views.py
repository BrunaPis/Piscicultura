from django.shortcuts import render, redirect
from app.form import PiscicultoresForm, PeixesForm
from app.form import ViveirosForm2, RacaoForm
from app.models import Piscicultores, Viveiros, Peixes, Racao
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
#from django.shortcuts import  HttpResponse


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')  # redirecionar para a página inicial após o login

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
def home (request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Piscicultores.objects.filter(piscicultor__icontains=search)
    else:
        data['db'] = Piscicultores.objects.all()
   # data['db']= Piscicultores.objects.all()
   # all = Piscicultores.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request,'index.html',data)

def form (request):
    data={}
    data['form']= PiscicultoresForm()
    return render(request,'form.html',data)

def create (request):
    form= PiscicultoresForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def view (request,pk):
    data = {}
    data['db'] = Piscicultores.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit (request,pk):
    data = {}
    data['db'] = Piscicultores.objects.get(pk=pk)
    data['form']=PiscicultoresForm(instance=data['db'])
    return render(request, 'form.html', data)

def update (request,pk):
    data = {}
    data['db'] = Piscicultores.objects.get(pk=pk)
    form = PiscicultoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete (request,pk):
    db= Piscicultores.objects.get(pk=pk)
    db.delete()
    return redirect('home')



def home2 (request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Viveiros.objects.filter(search)
    else:
        data['db'] = Viveiros.objects.all()
        return render(request, 'index.html', data)

def form2 (request):
    data={}
    data['form2']= ViveirosForm2()
    return render(request,'form2.html',data)


def create2 (request):
    form= ViveirosForm2(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home2')


def view2(request,pk):
    data = {}
    data['db'] = Viveiros.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit2 (request,pk):
    data = {}
    data['db'] = Viveiros.objects.get(pk=pk)
    data['form2']=ViveirosForm2(instance=data['db'])
    return render(request, 'form2.html', data)

def update2 (request,pk):
    data = {}
    data['db'] = Viveiros.objects.get(pk=pk)
    form2 = ViveirosForm2(request.POST or None, instance=data['db'])
    if form2.is_valid():
        form2.save()
        return redirect('home2')


def delete2 (request,pk):
    db= Viveiros.objects.get(pk=pk)
    db.delete()
    return redirect('home2')



def home3 (request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Peixes.objects.filter(search)
    else:
        data['db'] = Peixes.objects.all()
        return render(request, 'index.html', data)

def form3 (request):
    data={}
    data['form3']= PeixesForm()
    return render(request,'form3.html',data)

def create3 (request):
    form = ViveirosForm2(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home3')

def view3 (request,pk):
    data = {}
    data['db'] = Peixes.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit3 (request,pk):
    data = {}
    data['db'] = Peixes.objects.get(pk=pk)
    data['form']=PeixesForm(instance=data['db'])
    return render(request, 'form3.html', data)

def update3 (request,pk):
    data = {}
    data['db'] = Peixes.objects.get(pk=pk)
    form = PeixesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home3')

def delete3 (request,pk):
    db= Peixes.objects.get(pk=pk)
    db.delete()
    return redirect('home3')

def home4 (request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Racao.objects.filter(search)
    else:
        data['db'] = Racao.objects.all()
        return render(request, 'index.html', data)

def form4 (request):
    data={}
    data['form4']= RacaoForm()
    return render(request,'form4.html',data)

def create4 (request):
    form= RacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home4')

def view4 (request,pk):
    data = {}
    data['db4'] = Racao.objects.get(pk=pk)
    return render(request, 'view.html',data)

def edit4 (request,pk):
    data = {}
    data['db'] = Racao.objects.get(pk=pk)
    data['form4']=RacaoForm(instance=data['db'])
    return render(request, 'form4.html', data)

def update4 (request,pk):
    data = {}
    data['db'] = Racao.objects.get(pk=pk)
    form = RacaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home4')

def delete4 (request,pk):
    db= Racao.objects.get(pk=pk)
    db.delete()
    return redirect('home4')
