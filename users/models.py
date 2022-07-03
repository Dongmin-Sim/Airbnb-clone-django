from cgitb import html
import uuid, os
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import strip_tags
from django.template.loader import render_to_string

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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default='', blank=True)

    def verify_email(self):
        if not self.email_verified:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                'email//verify_email.html',
                {'secret':secret}
            )

            # send_mail(
            #     subject="Verify Airbnb Account",
            #     message=strip_tags(html_message),
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[self.email],
            #     fail_silently=False,
            #     html_message=html_message
            # )
            print(secret)
            print(settings.EMAIL_HOST_USER)
            self.save()

        return