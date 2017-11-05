from django.db import models

# Create your models here.

class BmiMeasurement(models.Model):
  height_in_meters = models.FloatField()
  weight_in_kilograms = models.FloatField()
  measured_at = models.DateField()

