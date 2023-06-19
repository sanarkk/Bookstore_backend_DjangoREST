from django.urls import path

from .views import RegisterAPI, LogoutAPI, LoginAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view()),
    path("logout/", LogoutAPI.as_view()),
    path("login/", LoginAPI.as_view()),
]
