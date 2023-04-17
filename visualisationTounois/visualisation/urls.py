from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('tournoi/<int:tournoi_id>/', views.tournoii, name='tournoii'),
    
]