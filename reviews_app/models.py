from django.db import models
from django.contrib.auth.models import User
from games_app.models import Game
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    """
    Representa una reseña de un juego.
    
    Attributes:
        user (ForeignKey): Referencia al usuario que creó la reseña.
        game (ForeignKey): Referencia al juego al que pertenece la reseña.
        title (CharField): Título de la reseña, con un máximo de 100 caracteres.
        review (TextField): Texto completo de la reseña.
        rating (PositiveIntegerField): Calificación del juego, con valores entre 1 y 5.
        created_at (DateTimeField): Fecha y hora en que se creó la reseña.
        updated_at (DateTimeField): Fecha y hora en que se actualizó la reseña.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE,related_name="reviews")
    title = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.title + " - " + str(self.user)
