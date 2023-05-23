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
    phone_number = serializers.CharField(required=True, allow_null=False)
    delivery_address = serializers.CharField(required=True, allow_null=False)

    class Meta:
        model = order
        fields = (
            "id",
            "user_name",
            "book",
            "phone_number",
            "country",
            "delivery_address",
        )

    def to_representation(self, instance):
        representation = dict()
        representation["Order ID"] = instance.id
        representation["Username"] = instance.user.username
        representation["First Name"] = instance.user.first_name
        representation["Last Name"] = instance.user.last_name
        representation["Book Name"] = instance.book.book_name
        representation["Book Price"] = instance.book.price
        representation["Book Author"] = instance.book.author.username
        representation["Country"] = instance.country
        representation["Phone Number"] = instance.phone_number
        representation["Delivery address"] = instance.delivery_address
        representation["Order Date"] = instance.date

        return representation


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
