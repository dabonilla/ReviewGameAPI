from rest_framework import serializers
from games_app.models import Game,Genre,Platform, Developer
from reviews_app.api.serializers import ReviewSerializer

class DeveloperSerializer(serializers.ModelSerializer):
    games = serializers.StringRelatedField(many=True)
    class Meta:
        model = Developer
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'
        
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
            
class GameSerializer(serializers.ModelSerializer):
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
