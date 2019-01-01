from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django_tables2 import SingleTableView
from django_tables2 import RequestConfig

from diocese.models.diocese_model import Archdiocese
from diocese.models.diocese_model import Diocese
from diocese.models.priest_model import Priest, PriestTable
import string



def index(request):
    archdiocese_list = Archdiocese.objects.all()
    context = {
        'archdiocese_list': archdiocese_list,
    }
    return render(request, 'diocese/index.html', context)

def alpha_priestlist(request):
    alphabet = string.ascii_uppercase
    context = {'alphabet': alphabet}
    return render(request, 'diocese/alphapriest_list.html', context)

def priest(request):
    table = PriestTable(Priest.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'diocese/priest_list.html', {'table': table})

def priestlist_view(request, letter=None):
    table = PriestTable(Priest.objects.all().filter(last_name__startswith=letter))
    RequestConfig(request).configure(table)
    return render(request, 'diocese/priest_list.html', {'table': table})


class DioceseDetailView(DetailView):
    model = Archdiocese

    def get_object(self):
        """Returns the Archdiocese instance that the view displays"""
        return get_object_or_404(Archdiocese, pk=self.kwargs.get("pk"))

class PriestList(SingleTableView):
    model = Priest
    context_object_name = 'priest_table'
    table_class = PriestTable
    def get_table_kwargs(self):
        return ( {'exclude': ('id','year_born','order_name','order_priest','offender',)}
        )
  
  
class ArchDioPriestListView(DetailView):
    model = Priest
    template_name = "diocese/all_diocese_priest_list.html"

    def get_object(self):
        """Returns the Archdiocese instance that the view displays"""
        return get_object_or_404(Archdiocese, pk=self.kwargs.get("pk"))

class DioPriestListView(DetailView):
    model = Priest

    def get_object(self):
        """Returns the Diocese instance that the view displays"""
        return get_object_or_404(Diocese, pk=self.kwargs.get("pk"))

  
class ArchPriestListView(DetailView):
    model = Priest
    template_name = "diocese/archdiocese_priest_list.html"

    def get_object(self):
        """Returns the Archdiocese instance that the view displays"""
        return get_object_or_404(Archdiocese, pk=self.kwargs.get("pk"))