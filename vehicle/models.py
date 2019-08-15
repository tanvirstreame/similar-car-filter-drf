from django.db import models

# Create your models here.

class Vehicle(models.Model):
  name = models.CharField(max_length=200)
  model = models.CharField(max_length=200)
  price = models.FloatField()
  odometer_reading = models.FloatField()
