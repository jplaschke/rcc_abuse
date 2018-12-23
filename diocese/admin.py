from django.contrib import admin
from .models import Diocese, Archdiocese, Statistics, Priest

admin.site.register(Diocese)
admin.site.register(Archdiocese)
admin.site.register(Statistics)
admin.site.register(Priest)

