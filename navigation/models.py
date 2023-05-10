from django.db import models
from account.models import User 


class UserCoordinate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_coordinates')
    coordinate_x = models.FloatField(null=True, blank=True)
    coordinate_y = models.FloatField(null=True, blank=True)