from django.shortcuts import render
from django.shortcuts import render

from diocese.models.diocese_model import Archdiocese
from diocese.models.diocese_model import Diocese

def index(request):
    archdiocese_list = Archdiocese.objects.order_by('name')
    context = {
        'archdiocese_list': archdiocese_list,
    }
    return render(request, 'diocese/index.html', context)
