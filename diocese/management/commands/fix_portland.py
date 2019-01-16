from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.diocese_model import Archdiocese
		from diocese.models.diocese_model import Diocese
		from diocese.models.priest_model import Priest

		portland_maine_diocese = Diocese.objects.get(name="Portland")
		portland_oregon_archdiocese = Archdiocese.objects.get(name="Portland in Oregon")
		
		portland_maine_priests = None
		portland_oregon_priests = None
		
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
			parsed_dio = parsed_line[7].split(",")
			dio_name = parsed_dio[0]
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
			if "Portland" in dio_name:
				state = parsed_dio[1].strip()
				if "OR" in state:
					dio_name = "Portland in Oregon"
				else:
					dio_name = "Portland"
				# find priest in database
				priest_list = Priest.objects.all().filter(first_name=first, \
								middle_name=middle, \
								last_name=last, \
								order_priest = True)
				priest = None
				if len(priest_list) > 1:
					priest = priest_list[0]
					print ("\n\nTOO MANY*****")
					count = 0
					for priest in priest_list:
						print ("last_name %s diocese_file %s arcdiocese %s dio %s" % (priest.last_name, parsed_dio, priest.archdiocese, priest.diocese))
						count += 1
						if count > 1:
							priest.delete()
				elif len(priest_list) > 0:
					priest = priest_list[0]
					print ("last_name %s diocese_file %s arcdiocese %s dio %s" % (priest.last_name, parsed_dio, priest.archdiocese, priest.diocese))
				else:
					print ("***** PRIEST NOT ADDED "+repr(last))
				if priest:
					if dio_name == "Portland":
						priest.archdiocese = None
						priest.diocese = portland_maine_diocese
					else:
						priest.archdiocese = portland_oregon_archdiocese
						priest.diocese = None
					print ("SAVE PRIEST "+repr(priest.order_priest))
					if priest.order_priest:
						priest.delete()
						