from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models import Order
		from django.utils.dateparse import parse_date
		in_file = open("./order_list_up.txt", "r")
		order_name = ""
		order_abbreviation = ""
		order_founder = ""
		order_family = ""
		order_founding_year = ""
		order_priest = True   # religious order priest or religious order brother
		for line in in_file:
			order_name = ""
			order_abbreviation = ""
			order_founder = ""
			order_family = ""
			order_founding_year = ""
			order_priest = True			
			if "Brother" in line:
				order_priest = False
			parsed_line = line.split("|") 
			order_name = str(parsed_line[0])
			try:
				order_abbreviation = parsed_line[1]
				order_founder = parsed_line[2]
				order_family = parsed_line[3]
				order_founding_year = parsed_line[4]
				order_founding_year = order_founding_year[:4]
			except Exception as e:
				print (repr(e)+" "+repr(parsed_line))
			try:
				order = Order(order_name = order_name, order_abbreviation=order_abbreviation, order_founder=order_founder,
								   order_family = order_family,
								 order_founding_year = order_founding_year)
				order.save()
			except Exception as e:
				print ("EXCEPT2"+repr(e)+" "+repr(parsed_line))
		in_file.close()