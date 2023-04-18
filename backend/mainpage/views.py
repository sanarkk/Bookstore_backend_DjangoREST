from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .permissions import IsOwner, IsMyProfile
from .models import book, order
from .serializers import (
    BookSerializer,
    CreateBookSerializer,
    UpdateBookSerializer,
    CreateOrderSerializer,
    UserProfileSerializer,
)


# Create your views here.
class ListBooksAPI(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        print(request.user)
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


class CreateOrderAPI(generics.CreateAPIView):
    queryset = book.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def post(self, request, *args, **kwargs):
        return self.create_order(request)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

    def create_order(self, request):
        instance = self.get_object()
        serializer = CreateOrderSerializer(instance, data=self.request.data)
        #print(instance)
        #print(serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    #def perform_create(self, serializer):
    #    serializer.save()


class ListUserInformation(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
