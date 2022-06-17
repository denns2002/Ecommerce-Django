from django.db import models
from .product import Products


class Evolutions(models.Model):
    class Meta:
        db_table = 'evolutions'
    pre_evolve_f = models.IntegerField(default=0)
    pre_evolve_s = models.IntegerField(default=0)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    next_evolve_f = models.IntegerField(default=0)
    next_evolve_s = models.IntegerField(default=0)
