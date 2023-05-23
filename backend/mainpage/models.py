from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    book_name = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return self.book_name


class order(models.Model):
    class DeliveryCountry(models.TextChoices):
        CANADA = "CA", ("Canada")
        UKRAINE = "UA", ("Ukraine")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(
        max_length=2, choices=DeliveryCountry.choices, default=DeliveryCountry.UKRAINE
    )
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} | {self.book.book_name}"
