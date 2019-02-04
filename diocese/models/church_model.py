from django.db import models
from django.utils.dateparse import parse_date

# Church models
class Church(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200,blank=True,null=True)
    zipcode = models.CharField(max_length=10,blank=True,null=True)
    lat = models.CharField(max_length=20,blank=True,null=True)
    lon = models.CharField(max_length=20,blank=True,null=True)
    city = models.CharField(max_length=40)
    county = models.CharField(max_length=40,blank=True,null=True)
    state = models.CharField(max_length=2)
    diocese = models.ForeignKey(
        'Diocese',
        on_delete=models.CASCADE,
    )
    establish_date = models.DateField('date established',blank=True,null=True)

    class Meta:
        unique_together = ('name', 'city', 'state')

    def __str__(self):
        return self.name


class ArchdioceseChurch(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200,blank=True,null=True)
    zipcode = models.CharField(max_length=10,blank=True,null=True)
    lat = models.CharField(max_length=20,blank=True,null=True)
    lon = models.CharField(max_length=20,blank=True,null=True)
    city = models.CharField(max_length=40,blank=True,null=True)
    state = models.CharField(max_length=2,blank=True,null=True)
    diocese = models.ForeignKey(
        'Archdiocese',
        on_delete=models.CASCADE,
    )
    establish_date = models.DateField('date established',blank=True,null=True)

    class Meta:
        unique_together = ('name', 'city', 'state')
		
    def __str__(self):
        return self.name

