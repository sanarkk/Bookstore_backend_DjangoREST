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
    OrderSerializer,
    UserProfileSerializer,
    UpdateUserProfileSerializer,
)


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


class GetOrderAPI(generics.RetrieveAPIView):
    queryset = book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


class CreateOrderAPI(generics.CreateAPIView):
    queryset = book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def post(self, request, *args, **kwargs):
        return self.create_order(request)

    def create_order(self, request):
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.user
        order.objects.create(
            user=user_id,
            book=instance,
            phone_number=request.data["phone_number"],
            country=request.data["country"],
            delivery_address=request.data["delivery_address"],
        )
        return Response()


class ListUserInformation(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        print(user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UpdateUserInformation(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def update(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated"})
        else:
            return Response({"message": "not updated"})


class ListUserOrders(generics.ListAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def get(self, request, *args, **kwargs):
        orders = order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ClearUserOrders(generics.CreateAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def post(self, request, *args, **kwargs):
        return self.clear_history(request)

    def clear_history(self, request):
        order.objects.filter(user=request.user).delete()
        return Response({"message": "orders history cleared"})
