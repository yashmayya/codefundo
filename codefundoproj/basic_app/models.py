from django.db import models

# Create your models here.

class UserData(models.Model):
    uid = models.CharField(max_length = 12, primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6)
