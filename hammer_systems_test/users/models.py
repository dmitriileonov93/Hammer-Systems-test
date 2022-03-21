from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .utils import generate_alphanum_random_string


class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, blank=True)
    owner_invite_code = models.CharField(max_length=6, editable=False)
    inviter_code = models.CharField(max_length=6, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return f'{str(self.phone_number)} - {self.owner_invite_code}'

    def save(self, *args, **kwargs):
        if not self.owner_invite_code:
            random_code = generate_alphanum_random_string(6)
            while User.objects.filter(owner_invite_code=random_code).exists():
                random_code = generate_alphanum_random_string(6)
            self.owner_invite_code = random_code
        self.set_password('1234')
        super().save(*args, **kwargs)
