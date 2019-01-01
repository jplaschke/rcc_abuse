from django.db import models
from django.utils.dateparse import parse_date
import django_tables2 as tables


# Order models

class Order(models.Model):
 
    order_name = models.CharField(max_length=230)
    order_abbreviation = models.CharField(max_length=30)
    order_priest = models.BooleanField(default=False)
    def __str__(self):
        return self.order_name+", "+self.order_abbreviation

