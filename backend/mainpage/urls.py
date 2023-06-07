from django.urls import path
from .views import (
    ListBooksAPI,
    CreateBookAPI,
    UpdateBookAPI,
    RetrieveBookAPI,
    CreateOrderAPI,
    GetOrderAPI,
    ListUserInformation,
    UpdateUserInformation,
    ListUserOrders,
    ClearUserOrders,
)

urlpatterns = [
    path("book/list", ListBooksAPI.as_view(), name="ListBooks"),
    path("book/create", CreateBookAPI.as_view(), name="CreateBook"),
    path("book/update/<int:pk>", UpdateBookAPI.as_view(), name="UpdateBook"),
    path("book/get/<int:pk>", RetrieveBookAPI.as_view(), name="GetOneBook"),
    path("order/create/<int:pk>",
         CreateOrderAPI.as_view(),
         name="CreateOrder"),
    path("order/get/<int:pk>", GetOrderAPI.as_view(), name="GetOrder"),
    path("profile/", ListUserInformation.as_view(), name="UserProfile"),
    path("profile/update",
         UpdateUserInformation.as_view(), name="UpdateUserProfile"),
    path("profile/orders", ListUserOrders.as_view(), name="ListOrders"),
    path("profile/orders/clear",
         ClearUserOrders.as_view(), name="ClearOrders"),
]
