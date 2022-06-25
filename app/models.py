from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, null=False,
                            unique=True, verbose_name='Nome')

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Nome')
    phone = models.CharField(max_length=15, null=False,
                             blank=False, verbose_name='Telefone')
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Cidade')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Nome')
    phone = models.CharField(max_length=15, null=False,
                             blank=False, verbose_name='Telefone')
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Cidade')

    def __str__(self):
        return self.name
