from rest_framework import serializers
from .models import book, order
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="author.username")

    class Meta:
        model = book
        fields = (
            "id",
            "book_name",
            "price",
            "user_name",
        )
        extra_kwargs = {"user_name": {"read_only": True}}


class CreateBookSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return book.objects.create(**validated_data)


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ("id", "book_name", "price")


class CreateOrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="author.username")
    book = serializers.CharField(source="book_name")

    class Meta:
        model = order
        fields = ("id", "user_name", "book")
        extra_kwargs = {"user": {"read_only": True}, "book": {"read_only": True}}

    def save(self, request, *args, **kwargs):
        order = super().save(request)
        book = self.data.get("book")
        user = self.data.get("user")
        order.book = book
        order.user = user
        order.save()
        return order


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
