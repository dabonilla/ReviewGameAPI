from django.db import models

class Developer (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    web_site = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ' - ' + self.country
    
class Genre (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Platform (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Game (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    launch_date = models.DateTimeField()
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')
    
    def __str__(self):
        return self.name +' - '+ str(self.developer)
    
    


    
