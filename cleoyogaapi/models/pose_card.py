from email.mime import image
from django.db import models


class PoseCard(models.Model):

    sanskrit_name = models.CharField(max_length=55)
    english_name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.URLField()
    level = models.ForeignKey("Level", on_delete=models.CASCADE)
    user = models.ForeignKey("CleoUser", on_delete=models.CASCADE)
