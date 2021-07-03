from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    registration_date = models.DateTimeField(auto_now_add=True)
    real_name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    email = models.EmailField(unique=True, max_length=255)
    birth_date = models.DateTimeField(null=True)
    photo = models.CharField(max_length=30)
    stacks = models.CharField(max_length=30)

    # apeal
    homepage = models.CharField(max_length=30)
    blog = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    description = models.TextField()
    feed_mail = models.EmailField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
