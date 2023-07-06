from django.shortcuts import render,redirect
from app.form import PiscicultoresForm
from app.models import Piscicultores
from django.core.paginator import Paginator
#from django.shortcuts import  HttpResponse

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



