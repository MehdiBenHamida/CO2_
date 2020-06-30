from django.db import models

# Create your models here.


class Co2Emission(models.Model):
    co2_rate = models.IntegerField()
    datetime = models.DateTimeField()
