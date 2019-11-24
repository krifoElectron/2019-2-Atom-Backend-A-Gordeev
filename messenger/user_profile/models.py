from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.TextField('о себе', max_length=500, blank=True)
    location = models.CharField('Местоположение', max_length=64, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    avatar = models.CharField(max_length=128, blank=True)
