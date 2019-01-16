from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.diocese_model import Archdiocese
		from diocese.models.diocese_model import Diocese
		from diocese.models.priest_model import Priest
		from diocese.models.order_model import Order
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
		in_file = open("./filtered.txt","r")
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
			notes = parsed_line[6]
			if clergy_type == 'N':
				print("\n\n\n****** NUN LINE *****")
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
			if not parsed_line[5]:
				parsed_line[5] = 'Diocesan'
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
					if order_priest:			
						order_count += 1
						order_priest.clergy_type = clergy_type
						order_priest.save()
					else:
						order_obj = None
						try:
							exception_caught = False
							order_obj = Order.objects.get(order_name=order_name)
						except Exception as e:
							print ("*****1111 Order exception: "+repr(e))
							exception_caught = True
						if exception_caught:
							print ("ATTEMPT TO Create order!!")
							order_abbreviation = "empty"
							order_founder = "empty"
							order_family = "empty"
							order_founding_year = "2019"
							print ("BEFORE create order???")
							try:
								order_obj = Order(order_name = order_name, order_abbreviation=order_abbreviation, \
											 order_founder=order_founder, \
											order_family = order_family, \
											order_founding_year = order_founding_year)
								print ("AFTER create order???")
								order_obj.save()
								print ("AFTER SAVE")
							except Exception as e1:
								print ("EXCEPTION Saved order = "+repr(e1))
						try:
							arch_obj = None
							dio_obj = None
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
							order_priest = Priest(first_name=first, \
								middle_name=middle, \
								last_name=last, \
								order_priest = True, \
								order = order_obj, \
								clergy_type = clergy_type, \
								diocese = dio_obj, archdiocese = arch_obj, \
								year_ordained=year_ordained)
							
							print ("SAVED ORDER CLERGY")
							order_priest.save()
						except Exception as ugg:
							print ("EXception "+repr(ugg))
							print ("ORDER PRIEST NOT SAVED" + repr(order_priest))

						missing_order_count += 1
					print ("ORDER priest :"+repr(order_priest))
				except Exception as huh:
					print ("DONT UNDERSTAND "+repr(huh))
					missing_order_count += 1
			elif parsed_line[5] == "" or parsed_line[5] == "Diocesan":
					
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
				if order_priest:
					if insert_dio:
						order_priest.diocese = dio_obj
					
					else:
						order_priest.archdiocese = arch_obj
					#order_priest.save()
				elif insert_dio:
					priest = Priest (first_name = first, middle_name = middle, last_name = last, \
								year_ordained = year_ordained, notes = notes, \
								diocese = dio_obj, clergy_type = clergy_type)
									
				elif insert_arch:
					priest = Priest (first_name = first, middle_name = middle, last_name = last, \
									year_ordained = year_ordained, notes = notes, \
									archdiocese = arch_obj, clergy_type = clergy_type)
				update_priest = None
				try:
					if insert_arch:
						update_priest = Priest.objects.all().filter(first_name=first, \
													middle_name=middle, \
													last_name=last, order_priest = False,\
													year_ordained=year_ordained, \
													 clergy_type = clergy_type, \
													archdiocese=arch_obj)
					else:
						update_priest = Priest.objects.all().filter(first_name=first, \
													middle_name=middle, \
													last_name=last, order_priest = False, \
													year_ordained=year_ordained, \
													 clergy_type = clergy_type, \
													diocese=dio_obj)					
				except:
					pass
				if update_priest:
					print ("UPDATE priest->"+repr(update_priest))
					update_priest[0].save()
					update_count += 1
					pass
				elif priest:
					print ("Save "+repr(priest)+" "+priest.clergy_type)
					save_count += 1
					priest.save()
				else:
					print ("ERROR "+repr(priest)+" "+repr(priest.clergy_type))
				
		print ("Saved count = "+repr(save_count))
		print ("updated count = "+repr(update_count))
		print ("order count = "+repr(order_count))
		print ("missing order count = "+repr(missing_order_count))
