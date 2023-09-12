from django.db import models


class AthleteClasses(models.Model):
    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    class_attended = models.ForeignKey("Classes", on_delete=models.CASCADE)
