from django.urls import path
from games_app.api.views import GenreListView,GenreDetailView,PlatformListView,PlatformDetailView, GameListView,GameDetailView,DeveloperDetailView,DeveloperListView

urlpatterns = [
    path('developer/',DeveloperListView.as_view(),name='developer-list'),
    path('developer/<int:pk>',DeveloperDetailView.as_view(),name='developer-detail'),
    
    path('genre/',GenreListView.as_view(),name='genre-list'),
    path('genre/<int:pk>',GenreDetailView.as_view(),name='genre-detail'),
    
    path('platform/',PlatformListView.as_view(),name='platform-list'),
    path('platform/<int:pk>',PlatformDetailView.as_view(),name='platform-detail'),
    
    path('game/',GameListView.as_view(),name='game-list'),
    path('game/<int:pk>',GameDetailView.as_view(),name='game-detail'),
]
