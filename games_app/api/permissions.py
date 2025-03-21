from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    """
    Permiso personalizado que permite acceso de solo lectura a todos los usuarios,
    pero restringe las operaciones de escritura (POST, PUT, DELETE) a los administradores.

    Methods:
        has_permission(request, view): Verifica si el usuario tiene permiso para la solicitud.
    """
    def has_permission(self, request):
        """
        Verifica si el usuario tiene permiso para realizar la solicitud.

        Args:
            request (HttpRequest): La solicitud HTTP.

        Returns:
            bool: True si el usuario tiene permiso, False en caso contrario.
        """
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_permission

class ReviewUserOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que permite acceso de solo lectura a todos los usuarios,
    pero restringe las operaciones de escritura (PUT, DELETE) al autor de la reseña o a los administradores.
    Methods:
        has_object_permission(request, view, obj): Verifica si el usuario tiene permiso para la solicitud.
    """
    def has_object_permission(self, request, obj):
        """
        Verifica si el usuario tiene permiso para realizar la solicitud sobre el objeto específico.

        Args:
            request (HttpRequest): La solicitud HTTP.
            obj (Review): El objeto de la reseña sobre el que se está realizando la solicitud.

        Returns:
            bool: True si el usuario tiene permiso, False en caso contrario.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff