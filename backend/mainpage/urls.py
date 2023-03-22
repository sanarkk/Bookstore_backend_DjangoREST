from django.urls import path
from .views import ListBooksAPI, CreateBookAPI, UpdateBookAPI, RetrieveBookAPI

urlpatterns = [
    path("main/", ListBooksAPI.as_view()),
    path("create/", CreateBookAPI.as_view()),
    path("update/<int:pk>", UpdateBookAPI.as_view()),
    path("main/<int:pk>", RetrieveBookAPI.as_view()),
]
