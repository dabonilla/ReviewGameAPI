from django.urls import path
from .views import (
    DeveloperListView, DeveloperDetailView,
    GenreListView, GenreDetailView,
    PlatformListView, PlatformDetailView,
    GameListView, GameDetailView
)
"""
Rutas para Developer:
  - 'developer/': Listar y crear desarrolladores (DeveloperListView).
  - 'developer/<int:pk>': Detalles, actualizar o eliminar un desarrollador (DeveloperDetailView).

Rutas para Genre:
  - 'genre/': Listar y crear géneros (GenreListView).
  - 'genre/<int:pk>': Detalles, actualizar o eliminar un género (GenreDetailView).

Rutas para Platform:
  - 'platform/': Listar y crear plataformas (PlatformListView).
  - 'platform/<int:pk>': Detalles, actualizar o eliminar una plataforma (PlatformDetailView).

Rutas para Game:
  - 'game/': Listar y crear juegos (GameListView). Incluye filtros y paginación.
  - 'game/<int:pk>': Detalles, actualizar o eliminar un juego (GameDetailView).
"""
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
