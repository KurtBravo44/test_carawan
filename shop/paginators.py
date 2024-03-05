from rest_framework.pagination import PageNumberPagination

class DefaultPaginator(PageNumberPagination):
    page_size = 10