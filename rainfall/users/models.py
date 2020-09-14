from django.contrib.auth.models import AbstractUser

from rainfall.core.models import SingletonModel


class User(AbstractUser, SingletonModel):
    pass