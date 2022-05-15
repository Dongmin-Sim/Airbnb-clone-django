from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):
    """ Review Model Difinition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', related_name="reviews", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.review} - {self.room}'