from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from .models import book
from .serializers import BookSerializer, CreateBookSerializer, UpdateBookSerializer


# Create your views here.
class ListBooksAPI(generics.ListAPIView):

    queryset = book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateBookAPI(generics.CreateAPIView):

    queryset = book.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveBookAPI(generics.RetrieveAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateBookAPI(generics.UpdateAPIView):

    queryset = book.objects.all()
    lookup_field = "pk"
    serializer_class = UpdateBookSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({"message": "updated"})
        else:
            return Response({"message": "not updated"})
