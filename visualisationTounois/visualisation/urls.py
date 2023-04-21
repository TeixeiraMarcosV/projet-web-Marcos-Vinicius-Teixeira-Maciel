from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('tournoi/<int:tournoi_id>/', views.tournoii, name='tournoii'),
    path('tournoi/<int:tournoi_id>/poule/<int:poule_id>/', views.poules, name='poules'),
    path('tournoi/<int:tournoi_id>/poule/match/<int:match_id>/', views.match, name='match'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tournoi/<int:tournoi_id>/poule/match/<int:match_id>/modif_comment/<int:comment_id>/', views.modifComment, name='modifComment'),
    
    #path('login/', views.login, name='login'),
    
    
    
    
]