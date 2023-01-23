from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime


class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, firstname, lastname, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_admin", True)
        other_fields.setdefault("is_superuser", True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                "is_staff must be True"
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "is_superuser must be True"
            )
        return self.create_user(email, password, firstname, lastname, **other_fields)

    def create_user(self, email, password, firstname, lastname, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def get_short_name(self):
        return self.firstname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def have_slot(self):
        last_slot = self.slots.last()
        if last_slot:
            slot_time = datetime.strptime(last_slot.time_slot, '%H:%M').time()
            return datetime.combine(last_slot.date, slot_time) > datetime.now()
        return False

    def get_upcoming_slot(self):
        if self.have_slot():
            return self.slots.last()
        return None
