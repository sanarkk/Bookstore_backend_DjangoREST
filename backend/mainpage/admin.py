from django.contrib import admin
from .models import Order, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Order)
