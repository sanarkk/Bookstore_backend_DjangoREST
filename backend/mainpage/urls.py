from django.urls import path
from .views import (
    ListBooksAPI,
    CreateBookAPI,
    UpdateBookAPI,
    RetrieveBookAPI,
    CreateOrderAPI,
    ListUserInformation,
    ListUserOrders,
)

urlpatterns = [
    path("main/", ListBooksAPI.as_view()),
    path("create/", CreateBookAPI.as_view()),
    path("update/<int:pk>", UpdateBookAPI.as_view()),
    path("main/<int:pk>", RetrieveBookAPI.as_view()),
    path("order/<int:pk>", CreateOrderAPI.as_view()),
    path("my-profile/<int:pk>", ListUserInformation.as_view()),
    path("my-orders/", ListUserOrders.as_view()),
]
