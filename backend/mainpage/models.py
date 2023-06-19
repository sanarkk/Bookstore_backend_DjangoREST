from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from bookstore.settings import LANGUAGE_CODE, LANGUAGES


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=7, choices=LANGUAGES, default=LANGUAGE_CODE
    )
    objects = models.Manager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user.username} - {self.language}"


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    book_name = models.CharField(max_length=60)
    price = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_name


class Order(models.Model):
    class DeliveryCountry(models.TextChoices):
        CANADA = "CA", _("Canada")
        UKRAINE = "UA", _("Ukraine")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message=_("Phone number must be entered in the format "
                          "'+123456789'. Up to 15 digits allowed."),
            ),
        ],
    )
    country = models.CharField(
        max_length=2,
        choices=DeliveryCountry.choices,
        default=DeliveryCountry.UKRAINE
    )
    delivery_address = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user.username} | {self.book.book_name}"
