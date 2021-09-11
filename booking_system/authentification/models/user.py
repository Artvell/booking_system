"""файл с моделью User"""
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from string import ascii_uppercase,ascii_lowercase , digits


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Email - обязательное поле')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Расширенная модель для хранения данных пользователя.
    Добавлено обязательное поле Роль.
    Поле email теперь обязательно и уникально
    """
    objects = UserManager()
    choices = [
        ("manager","manager"),
        ("admin","admin")
    ]
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,verbose_name="Роль",choices=choices)
    REQUIRED_FIELDS = ['role']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email
