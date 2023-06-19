from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Book, Order, Profile


class BookSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="author.username")

    class Meta:
        model = Book
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
        return Book.objects.create(**validated_data)


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "book_name", "price")


class OrderSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        allow_null=False,
        validators=[
            RegexValidator(
                r"^\+?1?\d{9,15}$",
                message=_("Enter a Valid Phone Number"),
            )
        ],
    )
    delivery_address = serializers.CharField(required=True, allow_null=False)

    class Meta:
        model = Order
        fields = (
            "id",
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
    language = serializers.CharField()
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name", "language")


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
