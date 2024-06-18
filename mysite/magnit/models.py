from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy
import uuid


def generate_unique_id():
    return uuid.uuid4().hex


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    unique_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255)
    # Add any additional fields you need for your user

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_username(username),
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    image = models.CharField(max_length=255)


class Statistics(models.Model):
    orders_count = models.IntegerField()
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)
