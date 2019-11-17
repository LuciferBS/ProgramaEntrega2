from django.shortcuts import render
from .models import Coment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def news_list(request):
    coments = Coment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Home\index.html',{'coments' : coments})

def detalle(request, pk):
    coments = get_object_or_404(Coment, pk = pk)
    return render(request, 'Home/generic.html',{'coments' : coments})
