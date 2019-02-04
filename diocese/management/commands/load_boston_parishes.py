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
		in_file = open("./boston_parish.txt","r")
		name = ""
		city = ""
		arch_obj = None
		dio_obj = None
		try:
			arch_obj = Archdiocese.objects.get(name="Boston")
		except Exception as e:
			#if dio_name == "Boston":
			#	print ("Excecption "+repr(e))
			sys.exit(-1)
		count = 0
		for line in in_file:
			parsed_line = line.split("|")
			name = parsed_line[0]
			city = parsed_line[1]
			state = "MA"
			try:
				print ("name "+repr(name)+"city = "+repr(city))
				parish = ArchdioceseChurch (name = name, city = city, state = state, \
								diocese = arch_obj)
				parish.save()
			except Exception as e:
				print ("EXCEPTION "+repr(e))
				pass