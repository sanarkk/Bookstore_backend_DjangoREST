from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.core.exceptions import ObjectDoesNotExist

from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get_or_create(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            Token.objects.create(user=user)
        return Response({"status": "created"})


class LogoutAPI(generics.GenericAPIView):
    def get(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)
        return Response({"response": "success"})


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        Token.objects.get_or_create(user=user)
        return Response({"status": "loggined"})
