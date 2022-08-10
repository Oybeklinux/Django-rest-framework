from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = '__all__'
    search_fields = ['^first_name', '^last_name']
    # ordering_fields = '__all__'


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
