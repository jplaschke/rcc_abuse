from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		from diocese.models.priest_model import Priest
		
		priest_list = Priest.objects.all()
		for priest in priest_list:
			# how many dups
			dup_list = Priest.objects.filter(first_name=priest.first_name, \
											middle_name=priest.middle_name, \
											last_name=priest.last_name, \
											year_ordained=priest.year_ordained, \
											diocese=priest.diocese, \
											archdiocese=priest.archdiocese)
			count = len(dup_list)
			count -= 1
			if count >= 1:
				print ("deleting dup: "+repr(priest))
			while count > 0:
				dup_list.delete()
				count -= 1
											
											
											