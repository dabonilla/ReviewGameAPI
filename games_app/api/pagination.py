from rest_framework.pagination import PageNumberPagination


class GamePagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    