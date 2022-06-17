from django.db import models


class Countries(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Manufacturers(models.Model):
    class Meta:
        db_table = 'manufacturers'
        verbose_name_plural = 'Manufacturers'
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200, blank=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ManufacturersNumbers(models.Model):
    class Meta:
        verbose_name_plural = 'Manufacturers Numbers'
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class ManufacturersEmails(models.Model):
    class Meta:
        verbose_name_plural = 'Manufacturers Emails'
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email
