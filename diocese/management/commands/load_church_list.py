from django.core.management.base import BaseCommand
import sys

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.diocese_model import Archdiocese
		from diocese.models.diocese_model import Diocese
		from diocese.models.church_model import Church
		from diocese.models.church_model import ArchdioceseChurch
		from diocese.models.priest_model import Priest
		
		from django.utils.dateparse import parse_date
		date_str = "2018-01-21"
		in_file = open("./church_list.txt","r")
		name = ""
		city = ""
		arch_obj = None
		dio_obj = None
	
		for line in in_file:
			#Our Lady Help of Christians|latlong|23 N Clinton St|East Orange|NJ|07017|Newark		
			parsed_line = line.split("|")
			name = parsed_line[0]
			address = parsed_line[2]
			city = parsed_line[3]
			state = parsed_line[4]
			zipcode = parsed_line[5]
			dio_name = parsed_line[6]
			dio_name = dio_name.strip()
			dio_found = False
			try:
				arch_obj = Archdiocese.objects.get(name=dio_name)
			except Exception as e:
				try:
					dio_obj = Diocese.objects.get(name=dio_name)
					dio_found = True
				except:
					print ("FAILED "+repr(dio_name))
					sys.exit(-1)
			count = 0
			try:
				if dio_found:
					print ("dio church name "+repr(name)+"city = "+repr(city))
					parish = Church (name = name, city = city, state = state, \
									diocese = dio_obj, address = address, zipcode = zipcode)
				else:
					print ("name "+repr(name)+"city = "+repr(city))
					parish = ArchdioceseChurch (name = name, city = city, state = state, \
									diocese = arch_obj, address = address, zipcode = zipcode)
				parish.save()
			except Exception as e:
				print ("EXCEPTION "+repr(e))
				pass