from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.translation import gettext_lazy as _

from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer


# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        message_success = _("Account created")
        message_failed = _("Account not created")

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
            return Response({f"{message_success}"})
        else:
            return Response({f"{message_failed}"})


class LogoutAPI(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    message_success = _("Logged out")
    message_failed = _("Not logged out")

    def get(self, request):
        return self.logout_user(request)

    def logout_user(self, request):
        if logout(request) is None:
            return Response({f"{self.message_success}"})
        else:
            return Response({f"{self.message_failed}"})


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    message_login = _("Logged in")

    @ensure_csrf_cookie
    def token_security(request):
        message = _("Successfully gave a cookie")
        return Response({f"{message}"})

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        Token.objects.get_or_create(user=user)
        return Response({f"{self.message_login}"})
