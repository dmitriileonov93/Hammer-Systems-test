from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from time import sleep

from .utils import generate_num_random_string


class VerifyCode(models.Model):
    phone = PhoneNumberField(null=False, blank=False)
    code = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        random_code = generate_num_random_string(4)
        self.code = random_code
        sleep(1)
        print('!!!!!!!!!!!!!')
        print(f'ВАШ КОД ВЕРИФИКАЦИИ: {self.code}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.phone}: {self.code}'
