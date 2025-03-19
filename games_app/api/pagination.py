from rest_framework.pagination import PageNumberPagination


class GamePagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'p'

class ReviewsPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    