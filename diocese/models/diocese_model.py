from django.db import models
from django.utils.dateparse import parse_date
from diocese.models.priest_model import Priest

# Diocese models
# A diocese has many stats rows
class Diocese(models.Model):
    archdiocese = models.ForeignKey(
        'Archdiocese',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    establish_date = models.DateField('date established')
    created_from = models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True) 

    def total_priests(self):
        return Priest.objects.filter(diocese__pk=self.pk).count()

    def priest_list(self):
        priest_list = list(Priest.objects.filter(diocese__pk=self.pk))
        return priest_list

    def __str__(self):
        return self.name


class Statistics(models.Model):
    diocese = models.ForeignKey(
        'Diocese',
        on_delete=models.CASCADE,
    )
    year = models.PositiveSmallIntegerField()
    total_priests = models.PositiveSmallIntegerField()
    num_parishes = models.PositiveSmallIntegerField()


class Archdiocese(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    mother_church_name = models.CharField(max_length=200)
    mother_church_address = models.CharField(max_length=200)
    mother_church_zipcode = models.CharField(max_length=200)
    establish_date = models.DateField('date established')

    def total_arch_priests(self):
        return Priest.objects.filter(archdiocese__pk=self.pk).count()

    def total_diocese_priests(self):
        count = 0
        for diocese in self.diocese_list():
            count += diocese.total_priests()
        return count

    def total_priests(self):
        return self.total_arch_priests() + self.total_diocese_priests()

    def diocese_list(self):
        diocese_list = list(Diocese.objects.filter(archdiocese__pk=self.pk))
        return diocese_list

    def __str__(self):
        return self.name

