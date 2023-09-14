from django.db import models
from django.contrib.auth.models import User


class AthleteClasses(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    class_attended = models.ForeignKey("Classes", on_delete=models.CASCADE)
