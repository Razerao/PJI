from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aviso/<int:id>', views.aviso, name = 'aviso'),
    path('ata/<int:id>', views.ata, name = 'ata'),
    path('outro/<int:id>', views.outro, name = 'outro'),
    path('comentarios/', views.comentarios, name = 'comentarios'),
    path('avisos/', views.avisos, name = 'avisos'),
    path('atas/', views.atas, name = 'atas'),
    path('outros/', views.outros, name = 'outros'),
]