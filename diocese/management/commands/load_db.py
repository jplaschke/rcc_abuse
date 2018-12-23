from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        from diocese.models import Archdiocese
        from diocese.models import Diocese
        states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
        from django.utils.dateparse import parse_date
        date_str = "2018-01-21"
        in_file = open(".\diocese.txt","r")
        name = ""
        city = ""
        state = ""
        mother_church_name = ""
        mother_church_address = ""
        mother_church_zipcode = ""
        arch_name = ""
        get_address = False
        get_city = False
        get_archdiocese = False
        establish_date = parse_date(date_str)
        insert_rec = False
        arch_obj = None
        for line in in_file:
            if "Diocese" in line:
                parsed_line = line.split(" ")
                name = " ".join(parsed_line[2:])
                name = str(name.strip())
                self.stdout.write( "diocese name "+repr(name) )
                get_archdiocese = True
            elif get_archdiocese:
                parsed_line = line.split(" ")
                if parsed_line[0] == 'arch':
                    arch_name = " ".join(parsed_line[1:])
                    arch_name = arch_name.title()
                    arch_name = arch_name.strip()
                    print ("arch name = "+repr(arch_name))
                get_archdiocese = False
                get_address = True
            elif get_address:
                self.stdout.write ("address line = "+repr(line))
                try:
                    arch_obj = Archdiocese.objects.get(name=arch_name)
                    insert_rec = True
                except Exception as e:
                    print ("Excecption "+repr(e))
                    pass
                mother_church_address = str(line)
                get_address = False
                get_city = True
            elif get_city:
                parsed_line = line.split(" ") 
                city = str(parsed_line[0])
                city = city.replace(",","")
                try:
                    state = states_dict[str(parsed_line[1])]
                    zip = str(parsed_line[2])
                    zip = zip.split("-")
                    zip = str(zip[0])
                    zip = zip.strip()
                    print ("address "+repr(mother_church_address))
                    print ("city "+repr(city))
                    print ("state "+repr(state))
                    print ("zip "+repr(zip))
                
                    diocese = Diocese(name = name, city=city, state=state,
                                   archdiocese = arch_obj,
                                 establish_date = establish_date)
                    '''
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
                    '''
                    diocese.save()
                    name = ""
                    city = ""
                    state = ""
                    mother_church_name = ""
                    mother_church_address = ""
                    arch_name = ""
                    mother_church_zipcode = ""               
                    get_archdiocese = False
                    get_city = False
                    arch_obj = None
                except:
                    pass