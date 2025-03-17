from django.contrib import admin
from games_app.models import Genre, Platform, Game, Developer
# Register your models here.
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Developer)
