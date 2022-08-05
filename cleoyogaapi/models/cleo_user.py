from django.db import models
from django.contrib.auth.models import User


class CleoUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    favorites = models.ManyToManyField("PoseCard", through='SavedPoseCard', related_name='favorites')