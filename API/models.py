from django.db import models
from .validators import min_value_validator, min_name_length_validator

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=55, validators=[min_name_length_validator], null=False, blank=False)
    value = models.FloatField(null=False, blank=False, validators=[min_value_validator])
    stock = models.IntegerField(null=False, blank=False, validators=[min_value_validator])
    discount_value = models.FloatField(null=True, blank=True, default=0)

