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
    path("get_book_list/", ListBooksAPI.as_view(), name="ListBooks"),
    path("create_book/", CreateBookAPI.as_view(), name="CreateBook"),
    path("update_book/<int:pk>", UpdateBookAPI.as_view(), name="UpdateBook"),
    path("get_book/<int:pk>", RetrieveBookAPI.as_view(), name="GetOneBook"),
    path("create_order/<int:pk>", CreateOrderAPI.as_view(), name="CreateOrder"),
    path("get_order/<int:pk>", GetOrderAPI.as_view(), name="GetOrder"),
    path("profile/", ListUserInformation.as_view(), name="UserProfile"),
    path("update_profile/", UpdateUserInformation.as_view(), name="UpdateUserProfile"),
    path("orders/", ListUserOrders.as_view(), name="ListOrders"),
    path("clear_orders/", ClearUserOrders.as_view(), name="ClearOrders"),
]
