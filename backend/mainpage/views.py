from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema

from .permissions import IsOwner, IsMyProfile
from .models import Book, Order, UserProfile
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
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        name="List all books",
        operation_description="This API endpoint allows "
                              "user to list all the books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateBookAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Create a book",
        operation_description="This API endpoint allows "
                              "user to create a book.",
        tags=["Book"],
    )
    def post(self, request, *args, **kwargs):
        return self.create_book(request)

    def create_book(self, request):
        serializer = CreateBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.user.id
        serializer.save(author_id=user_id)
        print(serializer.data)
        return Response({"message": "created"})


class RetrieveBookAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Get the book",
        operation_description="This API endpoint allows user to get a certain "
                              "book by ID.[only if an user is authenticated]",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateBookAPI(generics.UpdateAPIView):
    queryset = Book.objects.all()
    lookup_field = "pk"
    serializer_class = UpdateBookSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    http_method_names = ["put"]

    @swagger_auto_schema(
        name="Update information about the book",
        operation_description="This API endpoint allows "
                              "user to update information "
                              "about the book.[only if an "
                              "user is authenticated]",
        tags=["Book"],
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({"message": "updated"})
        else:
            return Response({"message": "not updated"})


class GetOrderAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "pk"

    @swagger_auto_schema(
        name="Get the order",
        operation_description="This API endpoint allows user to get the order "
                              "by ID.[only if an user is authenticated]",
        tags=["Order"],
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


class CreateOrderAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Create an order",
        operation_description="This API endpoint allows "
                              "user to create an order"
                              ".[only if an user is authenticated]",
        tags=["Order"],
    )
    def post(self, request, *args, **kwargs):
        return self.create_order(request)

    def create_order(self, request):
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.user
        Order.objects.create(
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

    @swagger_auto_schema(
        name="Get the user information",
        operation_description="This API endpoint allows "
                              "user to get information about his profile"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(id=request.user.id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UpdateUserInformation(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]
    http_method_names = ["put"]

    @swagger_auto_schema(
        name="Update profile information",
        operation_description="This API endpoint allows "
                              "user to update information of his profile"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def put(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated"})
        else:
            return Response({"message": "not updated"})


class ListUserOrders(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Get all user's orders",
        operation_description="This API endpoint allows"
                              " user to get all the orders of the user"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ClearUserOrders(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Clear orders history",
        operation_description="This API endpoint allows"
                              " user to clear user's order history"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def delete(self, request, *args, **kwargs):
        objects = Order.objects.filter(user=request.user)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
