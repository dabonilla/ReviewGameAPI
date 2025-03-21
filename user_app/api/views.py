from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user_app import models
from rest_framework import status

@api_view(['POST'])
def registration_view(request):
    """
    Vista para el registro de nuevos usuarios.

    Esta vista permite a los usuarios registrarse en el sistema.
    Si la solicitud es válida, se crea una nueva cuenta de usuario y se devuelve
    un token de autenticación (refresh y access).

    Args:
        request (HttpRequest): La solicitud HTTP con los datos del usuario.

    Returns:
        Response: Una respuesta HTTP con los datos del usuario y el token,
        o los errores de validación si la solicitud no es válida.
    """
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            #token = Token.objects.get(user=account).key
            #data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_200_OK)
@api_view(['POST',])
def logout_view(request):
    """
    Vista para cerrar la sesión de un usuario.

    Esta vista permite a los usuarios autenticados cerrar su sesión
    eliminando su token de autenticación.

    Args:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        Response: Una respuesta HTTP con estado 200 (OK) si la operación es exitosa.
    """
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)