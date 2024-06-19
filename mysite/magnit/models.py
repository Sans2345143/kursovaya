from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User
import uuid
from django.conf import settings


def generate_unique_id():
    return uuid.uuid4().hex


class CustomUser(AbstractUser):
    loyalty_points = models.IntegerField(default=0)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    unique_id = models.CharField(max_length=100, unique=True, blank=True, null=True, default=generate_unique_id)
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
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_promotion = models.BooleanField(default=False)
    special_offer = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return self.name

class LoyaltyLevel(models.Model):
    name = models.CharField(max_length=255)
    required_points = models.IntegerField()

    def __str__(self):
        return self.name


class LoyaltyPoints(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)