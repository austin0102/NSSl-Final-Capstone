from django.db import models
from django.contrib.auth.models import User


class Classes(models.Model):
    name = models.CharField(max_length=255)
    timeDate = models.DateTimeField()
    location = models.CharField(max_length=255)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_classes")
    difficulty = models.ForeignKey("Difficulty", on_delete=models.CASCADE, related_name="classes")
    price = models.DecimalField(max_digits=10, decimal_places=2)
