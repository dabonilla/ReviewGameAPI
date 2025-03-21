from games_app.models import Genre,Game,Platform, Developer
from games_app.api.serializers import GenreSerializer,PlatformSerializer, GameSerializer, DeveloperSerializer
from rest_framework import generics
from games_app.api import permissions, pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#DEVELOPER
class DeveloperListView(generics.ListCreateAPIView):
    """
    Vista para listar y crear desarrolladores.
    Solo los administradores pueden crear nuevos desarrolladores.

    Attributes:
        serializer_class (DeveloperSerializer): Serializador para el modelo Developer.
        queryset (QuerySet): Conjunto de todos los objetos Developer.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
    
class DeveloperDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para recuperar, actualizar y eliminar un desarrollador específico.
    Solo los administradores pueden actualizar o eliminar un desarrollador.

    Attributes:
        serializer_class (DeveloperSerializer): Serializador para el modelo Developer.
        queryset (QuerySet): Conjunto de todos los objetos Developer.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
# GENRE
class GenreListView(generics.ListCreateAPIView):
    """
    Vista para listar y crear géneros.
    Solo los administradores pueden crear nuevos géneros.

    Attributes:
        serializer_class (GenreSerializer): Serializador para el modelo Genre.
        queryset (QuerySet): Conjunto de todos los objetos Genre.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para recuperar, actualizar y eliminar un género específico.
    Permite a los usuarios autenticados ver los detalles de un género.

    Attributes:
        serializer_class (GenreSerializer): Serializador para el modelo Genre.
        queryset (QuerySet): Conjunto de todos los objetos Genre.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
# PLATFORM 
class PlatformListView(generics.ListCreateAPIView):
    """
    Vista para listar y crear plataformas.
    Solo los administradores pueden crear nuevas plataformas.

    Attributes:
        serializer_class (PlatformSerializer): Serializador para el modelo Platform.
        queryset (QuerySet): Conjunto de todos los objetos Platform.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para recuperar, actualizar y eliminar una plataforma específica.
    Permite a los usuarios autenticados ver los detalles de una plataforma.

    Attributes:
        serializer_class (PlatformSerializer): Serializador para el modelo Platform.
        queryset (QuerySet): Conjunto de todos los objetos Platform.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
    
#GAME
class GameListView(generics.ListCreateAPIView):
    """
    Vista para listar y crear juegos.

    Solo los administradores pueden crear nuevos juegos.
    Incluye filtros y búsqueda por nombre, géneros, plataformas y desarrolladores.

    Attributes:
        serializer_class (GameSerializer): Serializador para el modelo Game.
        queryset (QuerySet): Conjunto de todos los objetos Game.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
        filter_backends (list): Backends de filtrado (SearchFilter y DjangoFilterBackend).
        filterset_fields (list): Campos por los cuales se pueden filtrar los juegos.
        search_fields (list): Campos por los cuales se puede buscar.
        pagination_class (GamePagination): Clase de paginación personalizada.
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['genres__name','platforms__name', 'developer__name']
    search_fields = ['name']
    pagination_class = pagination.GamePagination
class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para recuperar, actualizar y eliminar un juego específico.
    Solo los administradores pueden actualizar o eliminar un juego.

    Attributes:
        serializer_class (GameSerializer): Serializador para el modelo Game.
        queryset (QuerySet): Conjunto de todos los objetos Game.
        permission_classes (list): Permisos requeridos para acceder a esta vista.
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [permissions.AdminOrReadOnly]