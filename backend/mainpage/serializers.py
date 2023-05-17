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


class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source="author.username", required=False, allow_null=True
    )
    book = serializers.CharField(source="book_name", required=False, allow_null=True)

    class Meta:
        model = order
        fields = ("id", "user_name", "book")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
