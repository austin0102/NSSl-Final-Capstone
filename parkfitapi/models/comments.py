from django.db import models
from django.contrib.auth.models import User
from parkfitapi.models import Classes


class Comments(models.Model):
    review = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="comments")
