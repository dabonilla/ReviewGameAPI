from games_app.models import Genre,Game,Platform, Developer
from games_app.api.serializers import GenreSerializer,PlatformSerializer, GameSerializer, DeveloperSerializer
from rest_framework import generics
from games_app.api import permissions

#DEVELOPER
class DeveloperListView(generics.ListCreateAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class DeveloperDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
# GENRE
class GenreListView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    
# PLATFORM 
class PlatformListView(generics.ListCreateAPIView):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
    
#GAME
class GameListView(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]