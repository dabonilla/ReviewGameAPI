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
    genres = serializers.StringRelatedField(many=True)
    platforms = serializers.StringRelatedField(many=True)
    developer = serializers.StringRelatedField()
    
    class Meta:
        model = Game
        fields = '__all__'