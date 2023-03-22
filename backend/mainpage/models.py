from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    book_name = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return self.book_name