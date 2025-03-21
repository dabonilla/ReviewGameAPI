from rest_framework.pagination import PageNumberPagination


class GamePagination(PageNumberPagination):
    """
    Paginación personalizada para la lista de juegos.

    Esta clase define la paginación para los juegos, permitiendo
    mostrar 15 elementos por página y utilizando el parámetro 'p'
    para especificar el número de página.

    Attributes:
        page_size (int): Número de elementos por página. Por defecto es 15.
        page_query_param (str): Parámetro de consulta para especificar el número de página.
        Por defecto es 'p'.
    """
    page_size = 15
    page_query_param = 'p'

class ReviewsPagination(PageNumberPagination):
    """
    Paginación personalizada para la lista de reseñas.

    Esta clase define la paginación para las reseñas, permitiendo
    mostrar 5 elementos por página y utilizando el parámetro 'p'
    para especificar el número de página.

    Attributes:
        page_size (int): Número de elementos por página. Por defecto es 5.
        page_query_param (str): Parámetro de consulta para especificar el número de página.
                               Por defecto es 'p'.
    """
    page_size = 5
    page_query_param = 'p'