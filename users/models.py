from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """
    
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    LANGUAGE_ENG = 'en'
    LANGUAGE_KOR = 'kr'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'English'),
        (LANGUAGE_KOR, 'Korean')
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'

    CURRENCY_CHOICES = ((CURRENCY_USD, "UDS"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(blank=True, upload_to="avatar")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOR)
    superhost = models.BooleanField(default=False)
