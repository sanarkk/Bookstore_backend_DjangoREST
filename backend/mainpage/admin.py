from django.contrib import admin
from .models import Order, Book, Profile


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("author", "book_name", "price")
    list_filter = ("price", )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "phone_number", "country")
    list_filter = ("user", "country")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "language")
