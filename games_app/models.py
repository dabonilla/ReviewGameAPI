from django.db import models

class Developer (models.Model):
    """
    Representa un desarrollador de videojuegos.

    Attributes:
        name (CharField): Nombre del desarrollador (único).
        description (CharField): Descripción del desarrollador.
        country (CharField): País de origen del desarrollador.
        web_site (CharField): Sitio web del desarrollador.

    Methods:
        __str__(): Devuelve una representación en cadena del desarrollador.
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    web_site = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ' - ' + self.country
    
class Genre (models.Model):
    """
    Representa un género de videojuegos.

    Attributes:
        name (CharField): Nombre del género (único).

    Methods:
        __str__(): Devuelve una representación en cadena del género.
    """
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
    
class Platform (models.Model):
    """
    Representa una plataforma de videojuegos.

    Attributes:
        name (CharField): Nombre de la plataforma (único).

    Methods:
        __str__(): Devuelve una representación en cadena de la plataforma.
    """
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
    
class Game (models.Model):
    """
    Representa un videojuego.

    Attributes:
        name (CharField): Nombre del juego.
        description (CharField): Descripción del juego.
        launch_date (DateTimeField): Fecha de lanzamiento del juego.
        genres (ManyToManyField): Géneros asociados al juego.
        platforms (ManyToManyField): Plataformas en las que está disponible el juego.
        developer (ForeignKey): Desarrollador del juego.
        avg_rating (FloatField): Calificación promedio del juego (por defecto 0).
        number_rating (IntegerField): Número de calificaciones recibidas (por defecto 0).

    Methods:
        __str__(): Devuelve una representación en cadena del juego.
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    launch_date = models.DateTimeField()
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name +' - '+ str(self.developer)
    
    


    
