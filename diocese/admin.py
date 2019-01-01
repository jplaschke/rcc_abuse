from django.contrib import admin
from .models import Diocese, Archdiocese, Statistics, Priest, Order

admin.site.register(Diocese)
admin.site.register(Archdiocese)
admin.site.register(Statistics)
admin.site.register(Priest)
admin.site.register(Order)

