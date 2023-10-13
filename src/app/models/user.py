from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

# Custom User manager
#----------------------------------------------------------------
class UserManager(BaseUserManager):
    def _create_user(self, user_name, email, 
                    password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_name=None, email=None, password=None, **extra_fields):
        return self._create_user(email, user_name, password, is_superuser=False, **extra_fields)

    def create_superuser(self, user_name, email, password, **extra_fields):
        user = self._create_user(user_name, email, password, is_staff=True, 
                                is_superuser=True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


# User models
# ----------------------------------------------------------------
class User(AbstractBaseUser, PermissionsMixin):
    company_id = models.PositiveIntegerField(_("company_ID"))
    user_name = models.CharField(_('User Name'), max_length=255, unique=True)
    name = models.CharField(_('Name'), blank=True, max_length=255)
    email = models.CharField(_('Email'), blank=True, max_length=255)
    phone = models.CharField(_('Phone'), blank=True, null=True, max_length=50)
    is_admin = models.BooleanField(_('Admin'), default=False)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['company_id', 'email']

    objects = UserManager()

    def __str__(self):
        return self.user_name