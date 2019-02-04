from django.core.management.base import BaseCommand
import sys

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.diocese_model import Archdiocese
		from diocese.models.diocese_model import Diocese
		from diocese.models.church_model import Church
		from diocese.models.church_model import ArchdioceseChurch
		from diocese.models.priest_model import Priest, ChurchAssignment
		
		from django.utils.dateparse import parse_date
		date_str = "2018-01-21"
		in_file = open("./assignment_list.txt","r")
		start_year = ""
		end_year = ""
		church_obj = None
		archchurch_obj = None
		church_name = ""
		first = ""
		middle = ""
		last = ""
		notes = ""
		state = ""
		city = ""
	
		for line in in_file:
			#Our Lady Help of Christians|latlong|23 N Clinton St|East Orange|NJ|07017|Newark		
			parsed_line = line.split("|")
			print ("parsed_line "+repr(parsed_line))
			start_year = parsed_line[0]
			try:
				end_year = parsed_line[1]
			except:
				end_year = " "
			church_name = parsed_line[2]
			city = parsed_line[3]
			state = parsed_line[4]
			first = parsed_line[5]
			middle = parsed_line[6]
			last = parsed_line[7]
			notes = parsed_line[8]
			notes = notes.strip()
			dio_found = False
			priest_found = False
			clergy_obj = None
			if len(middle) <= 0:
				middle = None
			try:
				if middle is not None:
					clergy_obj = Priest.objects.get(first_name=first, middle_name=middle, last_name=last)
				else:
					clergy_obj = Priest.objects.get(first_name=first, last_name=last)
			except Exception as e:
				print ("EXCEPTION = "+repr(e))
				sys.exit(-1)
				pass
			try:
				arch_obj = ArchdioceseChurch.objects.get(name=church_name,city=city,state=state)
			except Exception as e:
				try:
					dio_obj = Church.objects.get(name=church_name,city=city,state=state)
					dio_found = True
				except:
					print ("FAILED "+repr(church_name))
					sys.exit(-1)
			count = 0
			try:
				if clergy_obj is None:
					print ("ERRROR: clergy NOT found "+repr(last))
				else:
					if dio_found:
						print ("dio church name "+repr(church_name)+"city = "+repr(city))
						assignment = ChurchAssignment (start_year = start_year, end_year = end_year,  \
										diocese_church = dio_obj, notes = notes, clergy=clergy_obj)
					else:
						print ("name "+repr(church_name)+"city = "+repr(city))
						assignment = ChurchAssignment (start_year = start_year, end_year = end_year,  \
										archdiocese_church = arch_obj, notes = notes, clergy=clergy_obj)
				assignment.save()
			except Exception as e:
				print ("EXCEPTION "+repr(e))
				pass