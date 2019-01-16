from django.db import models
from django.utils.dateparse import parse_date
import django_tables2 as tables


# Priest models

class Priest(models.Model):
 
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30)
    year_born = models.CharField(max_length=4,blank=True,null=True)
    # year ordained or year of first assigment
    # create order enum
    order_priest = models.BooleanField(default=False)
    offender = models.BooleanField(default=True)
    year_ordained = models.CharField(max_length=16,blank=True,null=True)
    notes = models.CharField(max_length=5000)

    PRIEST = 'P'
    NUN = 'N'
    BROTHER = 'B'
    DEACON = 'D'
    SEMINARIAN = 'S'
    CLERGY_TYPE_CHOICES = (
        (PRIEST, 'Priest'),
        (NUN, 'Nun'),
        (BROTHER, 'Brother'),
        (SEMINARIAN, 'Seminarian'),
        (DEACON, 'Deacon'),
    )
    clergy_type = models.CharField(
        max_length=1,
        choices=CLERGY_TYPE_CHOICES,
        default=PRIEST,
    )
    diocese = models.ForeignKey(
        'Diocese',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )
    archdiocese = models.ForeignKey(
        'Archdiocese',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        'Order',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )  
    class Meta:
        unique_together = ('first_name', 'middle_name', 'last_name', 'year_ordained')

    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name

class ChurchAssignment(models.Model):
    start_date = models.DateField('start date',blank=True,null=True)
    end_date = models.DateField('end date',blank=True,null=True)
    # church
    archdiocese_church = models.ForeignKey(
        'ArchdioceseChurch',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )
    diocese_church = models.ForeignKey(
        'Church',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )


class DioceseAssignment(models.Model):
    # cardinal, archbiship, priest, order priest
    # create an enum
    position = models.CharField(max_length=10)
    start_date = models.DateField('start date',blank=True,null=True)
    end_date = models.DateField('end date',blank=True,null=True)
    # diocese or archdiocese
    archdiocese = models.ForeignKey(
        'Archdiocese',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )
    diocese = models.ForeignKey(
        'Diocese',
        blank=True,null=True,
        on_delete=models.CASCADE,
    )


class Deacon(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    year_born = models.CharField(max_length=4,blank=True,null=True)
    # year ordained or year of first assigment
    year_ordained = models.CharField(max_length=4,blank=True,null=True)
    priest = models.BooleanField(default=True)
    order_priest = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name


class PriestTable(tables.Table):  
    class Meta:
        model = Priest
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('last_name','first_name','middle_name',)
        exclude = ('id','year_born','order_name','order_priest','offender','order','clergy_type')


class NunTable(tables.Table):  
    class Meta:
        model = Priest
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('last_name','first_name','middle_name',)
        exclude = ('id','year_born','order_name','order_priest','offender','clergy_type')

class OrderPriestTable(tables.Table):  
    class Meta:
        model = Priest
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('last_name','first_name','middle_name',)
        exclude = ('id','year_born','order_name','order_priest','offender',)
