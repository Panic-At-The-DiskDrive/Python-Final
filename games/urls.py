from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.list_games, name='list_games'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('add-game/', views.add_game, name='add_game'),
    path('add-developer/', views.add_developer, name='add_developer'),
    path('add-platform/', views.add_platform, name='add_platform'),
    path('edit-game/<int:pk>/', views.edit_game, name='edit_game'), 
    path('delete-game/<int:pk>/', views.delete_game, name='delete_game'),
]





