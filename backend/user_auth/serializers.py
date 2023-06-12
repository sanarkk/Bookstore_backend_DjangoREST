from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from mainpage.models import Languages, UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, allow_null=False)
    last_name = serializers.CharField(required=True, allow_null=False)
    language = serializers.ChoiceField(
                                       choices=Languages)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "language",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            #userprofile=validated_data["MyUser"],
        )
        UserProfile.objects.get_or_create(
            user=user,
            language=validated_data["language"]
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class LogoutSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("username",)
