from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# https://testdriven.io/blog/django-custom-user-model/


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    # https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
    # wishlist = models.ManyToManyField() ****Need Alec's Album model****
    # rating = models.ManyToManyField() ****Need Alec's Album model****
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
