from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings


# Create your models here.


class languages(models.TextChoices):
    UKRAINIAN = "UA", ("Ukrainian")
    ENGLISH = "EN", ("English")


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2, choices=languages.choices, default=languages.ENGLISH
    )


class book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    book_name = models.CharField(max_length=60)
    price = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.book_name


class order(models.Model):
    class DeliveryCountry(models.TextChoices):
        CANADA = "CA", ("Canada")
        UKRAINE = "UA", ("Ukraine")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.",
            ),
        ],
    )
    country = models.CharField(
        max_length=2, choices=DeliveryCountry.choices, default=DeliveryCountry.UKRAINE
    )
    delivery_address = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user.username} | {self.book.book_name}"
