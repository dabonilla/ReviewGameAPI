from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('games_app.api.urls')),
    path('api/', include('reviews_app.api.urls')),
    path('account/', include('user_app.api.urls')),
]
