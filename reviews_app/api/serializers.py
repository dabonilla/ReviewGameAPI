from rest_framework import serializers
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Review.

    Este serializador convierte objetos Review en JSON y viceversa.
    Excluye el campo 'game' y marca el campo 'user' como de solo lectura.

    Attributes:
        Meta (class): Clase interna que define la configuración del serializador.
    """
    class Meta:
        model = Review
        exclude = ('game',)
        read_only_fields = ['user']