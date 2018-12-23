from diocese import models
from django.utils.dateparse import parse_date

# Diocese models

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