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
		in_file = open(".\priest_list.txt","r")
		first_name = ""
		middle = ""
		last = ""
		notes = ""
		arch_obj = None
		dio_obj = None
		save_count = 0
		update_count = 0
		missing_order_count = 0
		order_count = 0
		for line in in_file:
			parsed_line = line.split("|")
			add_priest = False
			#print ("line = "+repr(line))
			first = parsed_line[1]
			last = parsed_line[0]
			first_parsed = first.split(" ")
			first = first_parsed[0]
			clergy_type = parsed_line[3]
			order_name = parsed_line[5]
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
				dio_name = "Portland in Oregon"
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
			if not parsed_line[5]:
				continue
			order_priest = None
			if parsed_line[5] != "" and parsed_line[5] != "Diocesan":
				try:
					order_priest = Priest.objects.all().filter(first_name=first, \
								middle_name=middle, \
								last_name=last, \
								order_priest = True, \
								year_ordained=year_ordained)
					if len(order_priest) > 0:
						order_priest = order_priest[0]
					if order_priest and clergy_type == 'N':			
						order_count += 1
						order_priest.clergy_type = clergy_type
						order_priest.notes = notes
						order_priest.save()
					print ("ORDER priest :"+repr(order_priest))
				except:
					missing_order_count += 1
				
		print ("Saved count = "+repr(save_count))
		print ("updated count = "+repr(update_count))
		print ("order count = "+repr(order_count))
		print ("missing order count = "+repr(missing_order_count))
