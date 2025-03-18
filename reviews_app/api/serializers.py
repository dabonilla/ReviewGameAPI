from rest_framework import serializers
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    #game = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('game',)
        read_only_fields = ['user']