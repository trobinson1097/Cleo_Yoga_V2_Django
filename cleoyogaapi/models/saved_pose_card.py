from django.db import models


class SavedPoseCard(models.Model):

    user = models.ForeignKey("CleoUser", on_delete=models.CASCADE)
    pose_card = models.ForeignKey("PoseCard", on_delete=models.CASCADE)