from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    def __str__(self):
        return self.name


class UserGeo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='geo'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} geo"