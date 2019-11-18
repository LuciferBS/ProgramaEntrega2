from django.shortcuts import render
from .models import Coment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as do_logout

def news_list(request):
    user = request.user
    if user.has_perm('Home.adm'):
        coments = Coment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'Home/home.html',{'coments' : coments})
    else:
        return render(request, 'Home/index.html')

def detalle(request, pk):
    coments = get_object_or_404(Coment, pk = pk)
    return render(request, 'Home/generic.html',{'coments' : coments})

def logout(request):
    do_logout(request)
    return redirect('/')


    




