from django.db import models


class Types(models.Model):
    class Meta:
        db_table = 'types'
        verbose_name_plural = 'Types'
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
