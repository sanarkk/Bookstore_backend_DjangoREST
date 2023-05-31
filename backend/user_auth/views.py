from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import logout, login

from django.views.decorators.csrf import ensure_csrf_cookie

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
        return self.logout_user(request)

    def logout_user(self, request):
        if logout(request) == None:
            return Response({"response": "success"})
        else:
            return Response({"response": "failed"})


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @ensure_csrf_cookie
    def token_security(request):
        return Response({"status": "gave a cookie"})

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        Token.objects.get_or_create(user=user)
        return Response({"status": "loggined"})
