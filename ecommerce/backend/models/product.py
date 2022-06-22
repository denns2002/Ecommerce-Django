from django.db import models
from django.db import migrations

from .types import Types
from .manufacturers import Manufacturers


class Products(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name_plural = 'Products'
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10000)
    description = models.TextField(blank=True)


class Pictures(models.Model):
    class Meta:
        db_table = 'pictures'
        verbose_name_plural = 'Pictures'
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='pictures')
    url = models.ImageField(upload_to='pictures/pokemons/')

class PokemonTypes(models.Model):
    class Meta:
        db_table = 'pokemon_types'
        verbose_name_plural = 'Pokemon Types'
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)


class PokemonWeaknesses(models.Model):
    class Meta:
        db_table = 'pokemon_weaknesses'
        verbose_name_plural = 'Pokemon Weaknesses'
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
