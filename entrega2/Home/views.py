from django.shortcuts import render
from .models import Coment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as do_logout
from .forms import Recup, NoticiaForm

def news_list(request):
    user = request.user
    if user.has_perm('Home.adm'):
        coments = Coment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'Home/home.html',{'coments' : coments})
    else:
        coments = Coment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'Home/index.html',{'coments' : coments})

def detalle(request, pk):
    coments = get_object_or_404(Coment, pk = pk)
    return render(request, 'Home/generic.html',{'coments' : coments})

def logout(request):
    do_logout(request)
    return redirect('/')

def recuperar(request):
    form = Recup()
    return render(request, 'Home/recuperar.html', {'form': form})

def news_new(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date= timezone.now()
            news.save()
            
            return redirect('/')
    else:
        form = NoticiaForm()
    return render(request, 'Home/nueva.html',{'form' : form})

def news_edit(request, pk):
    coment = get_object_or_404(Coment, pk=pk)
    if request.method=="POST":
        form=NoticiaForm(request.POST, instance=coment)
        if form.is_valid():
            coment = form.save(commit=False)
            coment.author = request.user
            coment.published_date = timezone.now()
            coment.save()
            return  redirect('/')
    else:
        form = NoticiaForm(instance=coment)
    return render(request, 'Home/nueva.html',{'form':form})

def delete(request, pk):
    coment = get_object_or_404(Coment, pk=pk)
    coment.delete()
    return redirect('/')




