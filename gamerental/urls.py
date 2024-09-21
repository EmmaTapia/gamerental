from django.urls import path
from . import views 
from .views import add_platform, list_platforms

urlpatterns = [
    path('video_games/', views.list_video_games, name='list_video_games'),
    path('add-platform/', add_platform, name='add_platform'),
    path('list-platforms/', list_platforms, name='list_platforms'),  
    path('register_video_game/', views.register_video_game, name='register_video_game'),
    path('register_video_game/', views.register_video_game, name='register_video_game'),
    path('register_rental/', views.register_rental, name='register_rental'),
    path('rentals/', views.list_rentals, name='list_rentals'),
    path('video_games/genre/<int:genre_id>/', views.video_games_by_genre, name='video_games_by_genre'),
    path('video_games/platform/<int:platform_id>/', views.video_games_by_platform, name='video_games_by_platform'),
]