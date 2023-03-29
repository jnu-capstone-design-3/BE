from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Navigation(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="user_navi_history")
    history = models.JSONField(null=True, blank=True)


class Room(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_rooms')

    name = models.CharField(max_length=255, null=True, blank=True)
    user_list = models.TextField(null=True, blank=True)


class FriendList(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_friendlist',)
    friend_list = models.IntegerField(null=True, blank=True)