from django.forms import ValidationError
from rest_framework import generics
from reviews_app.api.serializers import ReviewSerializer
from reviews_app.models import Review
from games_app.models import Game
from games_app.api import permissions, pagination
from rest_framework import filters

class ReviewListView(generics.ListAPIView):
    """
    Vista  para recuperar una lista de reseñas de un juego específico.

    Attributes:
        serializer_class (ReviewSerializer): Serializador utilizado para las reseñas.
        pagination_class (ReviewsPagination): Clase de paginación utilizada.
        filter_backends (list): Lista de filtros aplicados a la vista.
        ordering_fields (list): Campos permitidos para ordenar los resultados.
    """
    serializer_class = ReviewSerializer
    pagination_class = pagination.ReviewsPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(game=pk)
class ReviewCreateView(generics.CreateAPIView):
    """
    Vista  para crear una nueva reseña de un juego.

    Attributes:
        serializer_class (ReviewSerializer): Serializador utilizado para las reseñas.
    
    """
    serializer_class = ReviewSerializer
    def get_queryset(self):
        """
        Retorna todas las reseñas.
        """
        return Review.objects.all()
    
    def perform_create(self, serializer):
        """
        Maneja la creación de una nueva reseña.
        
        - Recupera el juego usando el `pk` de los parámetros de la URL.
        - Verifica si el usuario ya ha reseñado el juego.
        - Actualiza la calificación promedio del juego y el número de calificaciones.
        - Guarda la reseña con el juego y el usuario asociado.
        
        Parámetros:
            serializer (ReviewSerializer): Instancia del serializador con los datos validados.
        """
        pk = self.kwargs['pk']
        game = Game.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(game=game,user=review_user)
        if review_queryset.exists():
            raise ValidationError('You have already reviewd this game')
        if game.number_rating == 0:
            game.avg_rating = serializer.validated_data['rating']
        else:
            game.avg_rating = (game.avg_rating + serializer.validated_data['rating'])/2
        game.number_rating = game.number_rating + 1
        game.save()
        serializer.save(game=game, user=review_user)
        
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista  para recuperar, actualizar o eliminar una reseña específica.

    Attributes:
        queryset (QuerySet): Conjunto de reseñas disponibles en la base de datos.
        serializer_class (ReviewSerializer): Serializador utilizado para las reseñas.
        permission_classes (list): Lista de permisos aplicados a la vista.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.ReviewUserOrReadOnly]
    