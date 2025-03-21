from rest_framework import serializers
from games_app.models import Game,Genre,Platform, Developer
from reviews_app.api.serializers import ReviewSerializer

class DeveloperSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Developer.

    Este serializador convierte objetos Developer en JSON y viceversa.
    Incluye todos los campos del modelo y un campo adicional `games`
    que muestra los nombres de los juegos asociados al desarrollador.

    Attributes:
        games (StringRelatedField): Campo que muestra los nombres de los juegos asociados.
    """
    games = serializers.StringRelatedField(many=True)
    class Meta:
        model = Developer
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Genre.

    Este serializador convierte objetos Genre en JSON y viceversa.
    Incluye todos los campos del modelo.
    """
    class Meta:
        model = Genre
        fields = '__all__'
        
class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Platform.

    Este serializador convierte objetos Platform en JSON y viceversa.
    Incluye todos los campos del modelo.
    """
    class Meta:
        model = Platform
        fields = '__all__'
            
class GameSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Game.

    Este serializador convierte objetos Game en JSON y viceversa.
    Incluye todos los campos del modelo y campos adicionales para
    las relaciones con los modelos Review, Platform, Developer y Genre.

    Attributes:
        reviews (ReviewSerializer): Campo que muestra las reseñas asociadas al juego.
        platforms (SlugRelatedField): Campo que permite asignar plataformas por su nombre.
        developer (SlugRelatedField): Campo que permite asignar un desarrollador por su nombre.
        genres (SlugRelatedField): Campo que permite asignar géneros por su nombre.
    """
    reviews = ReviewSerializer(many=True, read_only=True)
    
    platforms = serializers.SlugRelatedField(
        queryset=Platform.objects.all(),
        slug_field='name',  
        many=True  # Indica que es una relación many-to-many
    )
    developer = serializers.SlugRelatedField(
        queryset=Developer.objects.all(),
        slug_field='name'  
    )
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='name',
        many=True  
    )
    class Meta:
        model = Game
        fields = '__all__'
