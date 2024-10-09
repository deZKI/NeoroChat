from django.db import models
from django.contrib.auth.models import AbstractUser


class UserExtended(AbstractUser):
    """ Пользователь (расширенная модель) """
    username = models.CharField(max_length=50, unique=True, verbose_name='Telegram ID', blank=True, null=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id", ]
