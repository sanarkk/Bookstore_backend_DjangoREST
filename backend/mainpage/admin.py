from django.contrib import admin
from .models import order, book

# Register your models here.
admin.site.register(book)
admin.site.register(order)