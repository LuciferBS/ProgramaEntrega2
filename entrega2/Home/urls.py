from django.urls import path
from . import views

urlpatterns = [
    path ('', views.news_list, name='coment_list'),
    path ('noticia',views.detalle, name='generic'),
]