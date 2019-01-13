from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.diocese_model import Archdiocese
		from diocese.models.diocese_model import Diocese
		from diocese.models.priest_model import Priest
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
		in_file = open(".\priest.txt","r")
		first_name = ""
		middle = ""
		last = ""
		notes = ""
		arch_obj = None
		dio_obj = None
		count = 0
		for line in in_file:
			parsed_line = line.split("|")
			add_priest = False
			if parsed_line[5] == "":
				first = parsed_line[1]
				last = parsed_line[0]
				first_parsed = first.split(" ")
				first = first_parsed[0]
				clergy_type = parsed_line[3]
				try:
					middle = first_parsed[1]
					middle = middle.replace(".","")
				except:
					middle = ""
				notes = parsed_line[6]
				year_ordained = parsed_line[2]
				parsed_dio = parsed_line[7].split(",")
				dio_name = parsed_dio[0]
				if "none" in dio_name:
					print ("line = "+repr(line))
				if dio_name == "Washington":
					dio_name = "Washington DC"
				if dio_name == "Kansas City":
					dio_name = "Kansas City in Kansas"
				if dio_name == "Portland":
					if parsed_dio[1] == "OR":
						dio_name = "Portland in Oregon"
					else:
						dio_name = "Portland"
				if dio_name == "St. Paul-Minneapolis":
					dio_name = "St. Paul and Minneapolis"
				if dio_name == "Springfield":
					if parsed_dio[1] == "MO":
						dio_name = "Springfield-Cape Girardeau"
					elif parsed_dio[1] == "IL":
						dio_name = "Springfield in Illinois"
					else:
						dio_name = "Springfield in Massachusetts"
				
				if dio_name == "Lafayette":
					if parsed_dio[1] == "IN":
						dio_name = "Lafayette in Indiana"
					else:
						dio_name = "Lafayette in Louisiana"
					
				insert_arch = False
				insert_dio = False
				try:
					arch_obj = Archdiocese.objects.get(name=dio_name)
					insert_arch = True
				except Exception as e:
					#if dio_name == "Boston":
					#	print ("Excecption "+repr(e))
					pass
				insert_dio = False
				try:
					dio_obj = Diocese.objects.get(name=dio_name)
					insert_dio = True
				except Exception as e:
					if "Wheeling" in dio_name:
						print ("Excecption "+repr(e))
					pass
				count = 0
				if insert_dio and count == 0:
					priest = Priest (first_name = first, middle_name = middle, last_name = last, \
								year_ordained = year_ordained, notes = notes, \
								diocese = dio_obj, clergy_type = clergy_type)
									
				if insert_arch and count == 0:
					priest = Priest (first_name = first, middle_name = middle, last_name = last, \
									year_ordained = year_ordained, notes = notes, \
									archdiocese = arch_obj, clergy_type = clergy_type)
				if priest:
					print ("Save "+priest+" "+priest.clergy_type)
					count += 1
					priest.save()
				else:
					print ("Save "+repr(priest)+" "+repr(priest.clergy_type))
				
		print ("Inserted = "+repr(count))