from django.db import models
from django.utils.dateparse import parse_date

# Church models
class Church(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    lat = models.CharField(max_length=200,blank=True,null=True)
    lon = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    diocese = models.ForeignKey(
        'Diocese',
        on_delete=models.CASCADE,
    )
    establish_date = models.DateField('date established')
    def __str__(self):
        return self.name


class ArchdioceseChurch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    lat = models.CharField(max_length=200,blank=True,null=True)
    lon = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    diocese = models.ForeignKey(
        'Archdiocese',
        on_delete=models.CASCADE,
    )
    establish_date = models.DateField('date established')
    def __str__(self):
        return self.name

