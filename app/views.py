from django.shortcuts import render, redirect, get_object_or_404

from app.form import PiscicultoresForm, ViveirosForm, PeixesForm, RacaoForm
from app.models import Piscicultores, Viveiros, Peixes, Racao


# from django.shortcuts import  HttpResponse

def login(request):
    return render(request,'login.html')

def Index(request):
    return render(request, 'Index.html')

def home(request):
    return render(request, 'home.html')





def create_racao(request):
    return render(request, 'create_racao.html')



def viewsracao(request):
    return render(request, 'viewsracao.html')








def create_piscicultor(request):
    if request.method == 'POST':
        form = PiscicultoresForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('IndexPiscicultor')
    else:
        form = PiscicultoresForm
    return render(request, 'create_piscicultor.html', {'formPiscicultor': form})


def IndexPiscicultor(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Piscicultores.objects.filter(app__icontains=search)
    else:
        data['db'] = Piscicultores.objects.all()
    return render(request, 'IndexPiscicultor.html', data)


def viewspiscicultor(request, pk):
    data = {}
    data['db'] = Piscicultores.objects.get(pk=pk)
    return render(request, 'viewspiscicultor.html', data)

def editPiscicultor(request, pk):
    data = {}
    data['db'] = Piscicultores.objects.get(pk=pk)
    data['formPiscicultor'] = PiscicultoresForm(instance=data['db'])
    return render(request, 'create_piscicultor.html', data)




def updatePiscicultor(request, pk):
    piscicultores = get_object_or_404(Piscicultores, pk=pk)
    if request.method == 'POST':
        form = PiscicultoresForm(request.POST, instance=piscicultores)
        if form.is_valid():
            form.save()
            return redirect('IndexPiscicultor')
    else:
        form = PiscicultoresForm(instance=piscicultores)
    return render(request, 'create_piscicultor.html', {'formPiscicultor': form})



def deletePiscicultor(request, pk):
    db = Piscicultores.objects.get(pk=pk)
    db.delete()
    return redirect('IndexPiscicultor')




def create_viveiro(request):
    if request.method == 'POST':
        form = ViveirosForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('IndexViveiro')
    else:
        form = ViveirosForm()
    return render(request, 'create_viveiro.html', {'formViveiro': form})

def IndexViveiro(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Viveiros.objects.filter(app__icontains=search)
    else:
        data['db'] = Viveiros.objects.all()
    return render(request, 'IndexViveiro.html', data)

def viewsviveiro(request, pk):
    data = {}
    data['db'] = Viveiros.objects.get(pk=pk)
    return render(request, 'viewsviveiro.html', data)


def editViveiro(request, pk):
    data = {}
    data['db'] = Viveiros.objects.get(pk=pk)
    data['formViveiro'] = ViveirosForm(instance=data['db'])
    return render(request, 'create_viveiro.html', data)


def updateViveiro(request, pk):
    Viveiros = get_object_or_404(Viveiros, pk=pk)
    if request.method == 'POST':
        form = Viveiros(request.POST, instance=Viveiros)
        if form.is_valid():
            form.save()
            return redirect('IndexViveiro')
    else:
        form = Viveiros(instance=Viveiros)
    return render(request, 'create_viveiro.html', {'formviveiro': form})



def deleteViveiro(request, pk):
    db = Viveiros.objects.get(pk=pk)
    db.delete()
    return redirect('IndexViveiro')



def create_peixe(request):
    if request.method == 'POST':
        form = PeixesForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('IndexPeixe')
    else:
        form = PeixesForm()
    return render(request, 'create_peixe.html', {'formPeixe': form})

def IndexPeixe(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Peixes.objects.filter(app__icontains=search)
    else:
        data['db'] = Peixes.objects.all()
    return render(request, 'IndexPeixe.html', data)

def editPeixe(request, pk):
    data = {}
    data['db'] = Peixes.objects.get(pk=pk)
    data['formPeixe'] = PeixesForm(instance=data['db'])
    return render(request, 'create_peixe.html', data)


def viewspeixe(request, pk):
    data = {}
    data['db'] = Peixes.objects.get(pk=pk)
    return render(request, 'viewspeixe.html', data)



def updatePeixe(request, pk):
    Peixes = get_object_or_404(Peixes, pk=pk)
    if request.method == 'POST':
        form = PeixesForm(request.POST, instance=Peixes)
        if form.is_valid():
            form.save()
            return redirect('IndexPeixe')
    else:
        form = PeixesForm(instance=Peixes)
    return render(request, 'create_peixe.html', {'formPeixe': form})



def deletePeixe(request, pk):
    db = Peixes.objects.get(pk=pk)
    db.delete()
    return redirect('IndexPeixe')




def create_racao(request):
    if request.method == 'POST':
        form = RacaoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('IndexRacao')
    else:
        form = RacaoForm()
    return render(request, 'create_racao.html', {'formRacao': form})


def IndexRacao(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Racao.objects.filter(app__icontains=search)
    else:
        data['db'] = Racao.objects.all()
    return render(request, 'IndexRacao.html', data)

def viewsracao(request, pk):
    data = {}
    data['db'] = Racao.objects.get(pk=pk)
    return render(request, 'viewsracao.html', data)


def editRacao(request, pk):
    data = {}
    data['db'] = Racao.objects.get(pk=pk)
    data['formRacao'] = RacaoForm(instance=data['db'])
    return render(request, 'create_racao.html', data)


def updateRacao(request, pk):
    racao_instance = get_object_or_404(Racao, pk=pk)
    if request.method == 'POST':
        form = RacaoForm(request.POST, instance=racao_instance)
        if form.is_valid():
            form.save()
            return redirect('IndexRacao')
    else:
        form = RacaoForm(instance=racao_instance)
    return render(request, 'create_racao.html', {'formRacao': form})




def deleteRacao(request, pk):
    db = Racao.objects.get(pk=pk)
    db.delete()
    return redirect('IndexRacao')