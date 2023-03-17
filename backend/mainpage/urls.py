from django.urls import path
from .views import list_movies, create_book, update_book, retrieve_book

urlpatterns = [
    path('main/', list_movies.as_view()),
    path('create/', create_book.as_view()),
    path('update/<int:id>', update_book.as_view()),
    path('main/<int:pk>', retrieve_book.as_view()),
]