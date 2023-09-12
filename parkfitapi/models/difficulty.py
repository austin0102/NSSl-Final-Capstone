from django.db import models

class Difficulty(models.Model):
    skillLevel = models.CharField(max_length=255)