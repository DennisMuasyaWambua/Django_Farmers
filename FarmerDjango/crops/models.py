from django.db import models


# Create your models here.
class Soil(models.Model):
    n = models.DecimalField(decimal_places=2, max_digits=8)
    p = models.DecimalField(decimal_places=2, max_digits=8)
    k = models.DecimalField(decimal_places=2, max_digits=8)
    temperature = models.DecimalField(decimal_places=2, max_digits=8)
    humidity = models.DecimalField(decimal_places=2, max_digits=8)
    ph = models.DecimalField(decimal_places=2, max_digits=8)
    rainfall = models.DecimalField(decimal_places=2, max_digits=8)
