from django.urls import path
from user_app.api.views import registration_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

"""

Rutas para autenticación:
- 'login/': Obtiene un token JWT para autenticación (TokenObtainPairView).
- 'token/refresh/': Refresca un token JWT (TokenRefreshView).

Rutas para registro y gestión de usuarios:
- 'register/': Registra un nuevo usuario (registration_view).
- 'logout/': Cierra la sesión de un usuario (logout_view) [Comentada].

"""
urlpatterns = [
    #path('login/', obtain_auth_token, name = 'login'),
    path('register/', registration_view, name = 'register'),
    #path('logout/', logout_view, name = 'logout'),
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    
]
