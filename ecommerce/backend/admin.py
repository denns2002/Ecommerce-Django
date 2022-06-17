from django.contrib import admin

from .models.evolutions import Evolutions
from .models.product import Products, Pictures, PokemonTypes, PokemonWeaknesses
from .models.manufacturers import Countries, Manufacturers, ManufacturersNumbers, ManufacturersEmails
from .models.types import Types


class CountryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    filter_fields = ['__str__']
    search_fields = ['__str__']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_fields = ['name']
    search_fields = ['name']


class PicturesInline(admin.TabularInline):
    model = Pictures


class PokemonTypesInline(admin.TabularInline):
    model = PokemonTypes


class PokemonWeaknessesInline(admin.TabularInline):
    model = PokemonWeaknesses


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'manufacturer', 'price']
    filter_fields = ['number', 'name', 'manufacturer', 'price']
    inlines = (
        PicturesInline,
        PokemonTypesInline,
        PokemonWeaknessesInline,
    )


class NumberInline(admin.TabularInline):
    model = ManufacturersNumbers


class EmailInline(admin.TabularInline):
    model = ManufacturersEmails


class ManufacturersAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    inlines = (
        NumberInline,
        EmailInline,
    )


# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Countries, CountryAdmin)
admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Evolutions)