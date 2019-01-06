from django.db import models
from django.utils.dateparse import parse_date
import django_tables2 as tables
from diocese.models.priest_model import Priest


# Order models

class Order(models.Model):
 
    order_name = models.CharField(max_length=230)
    order_abbreviation = models.CharField(max_length=30)
    order_founder = models.CharField(max_length=230,blank=True,null=True)
    order_family = models.CharField(max_length=50,blank=True,null=True)
    order_founding_year = models.CharField(max_length=4,blank=True,null=True)
    order_priest = models.BooleanField(default=False)   # religious order priest or religious order brother

    def total_priests(self):
        return Priest.objects.filter(order__pk=self.pk).count()

    def priest_list(self):
        priest_list = list(Priest.objects.filter(order__pk=self.pk))
        return priest_list

    def __str__(self):
        return self.order_name+", "+self.order_abbreviation

