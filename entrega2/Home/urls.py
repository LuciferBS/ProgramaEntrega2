from django.urls import path
from . import views

urlpatterns = [
    path ('', views.news_list, name='coment_list'),
    path ('noticia/<int:pk>/',views.detalle, name='detail'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('Noti/nueva/', views.news_new, name='news_new'),
    path('Noti/<int:pk>/edit',views.news_edit, name='news_edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    
]