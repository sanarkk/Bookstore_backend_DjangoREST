from rest_framework import serializers
from .models import book


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
