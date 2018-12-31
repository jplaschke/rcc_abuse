import django_tables2 as tables
from .models import Archdiocese

class DioceseTable(tables.Table):
	class Meta:
		model = Archdiocese
		