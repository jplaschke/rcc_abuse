from django.db import models
from django.utils.dateparse import parse_date

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
    def __str__(self):
        return self.name

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

class Priest(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    year_born = models.CharField(max=4,blank=True,null=True)
    # year ordained or year of first assigment
    year_ordained = models.CharField(max=4,blank=True,null=True)
    priest = forms.BooleanField(initial=True)
    order_priest = forms.BooleanField(initial=False)
    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name


class Deacon(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name+" "+self.middle_name

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

    def __str__(self):
        return self.name

if __name__ == "__main__":
    date_str = "2018-01-21"
    in_file = open("./diocese.txt","r")
    name = ""
    city = ""
    state = ""
    mother_church_name = ""
    mother_church_address = ""
    mother_church_zipcode = ""
    establish_date = parse_date(date_str)
    for line in in_file:
        name = ""
        city = ""
        state = ""
        mother_church_name = ""
        mother_church_address = ""
        mother_church_zipcode = ""
        get_address = False
        if "Archdiocese" in line and not get_address:
            parsed_line = line.split(" ")
            name = str(parsed_line[2].strip())
            print( "diocese name "+repr(name) )
            get_address = True
        elif get_address:
            print ("address line = "+repr(line))
            get_address = False