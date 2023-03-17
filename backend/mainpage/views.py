from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import book
from .serializers import book_serial, bookreate, update_book


# Create your views here.
class list_movies(generics.ListAPIView):

    queryset = book.objects.all()
    serializer_class = book_serial

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class create_book(generics.CreateAPIView):

    queryset = book.objects.all()
    serializer_class = bookreate

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class retrieve_book(generics.RetrieveAPIView):
    queryset = book.objects.all()
    serializer_class = book_serial
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class update_book(generics.UpdateAPIView):

    queryset = book.objects.all()
    lookup_field = 'id'
    serializer_class = update_book

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated"})
        else:
            return Response({"message": "not updated"})