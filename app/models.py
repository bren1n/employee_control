from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

class Role(models.Model):
    name = models.CharField(max_length=50, null=False)


class Manager(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)