from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    
    """ Time Stamped Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # abstract model : 추상 클래스, DB에는 반영되지 않음