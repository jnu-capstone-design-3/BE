from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
    '''
    Django에서 기본 제공하는 User Model은 username이 필수로 들어가기 때문에
    AbstractUser을 상속받아서 이메일만 사용할 수 있도록 커스텀
    '''

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class User(AbstractUser) :
#     pass

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