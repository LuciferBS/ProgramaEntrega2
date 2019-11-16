from django.shortcuts import render
from .models import Coment
from django.utils import timezone

def news_list(request):
    coments = Coment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Home\index.html',{'coments' : coments})

def detalle(request):
    return render(request, 'Home\generic.html',{})
