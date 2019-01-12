from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django_tables2 import SingleTableView
from django_tables2 import RequestConfig

from diocese.models.diocese_model import Archdiocese
from diocese.models.diocese_model import Diocese
from diocese.models.priest_model import Priest, PriestTable, OrderPriestTable
from diocese.models.order_model import Order
import string



def index(request):
    archdiocese_list = Archdiocese.objects.all()
    total_dio_priests = Priest.objects.filter(order_priest=False).count()
    total_order_priests = Priest.objects.filter(order_priest=True).count()
    context = {
        'archdiocese_list': archdiocese_list,
        'total_priests': total_dio_priests+total_order_priests,
        'total_dio_priests': total_dio_priests,
        'total_order_priests': total_order_priests,
    }
    return render(request, 'diocese/index.html', context)


def order(request):
    order_list = sorted([ i for i in Order.objects.all() if i.total_priests() > 0], key=lambda x: x.total_priests(),reverse=True)
    #total_dio_priests = Priest.objects.filter(order_priest=False).count()
    #total_order_priests = Priest.objects.filter(order_priest=True).count()
    context = {
        'order_list': order_list,
        #'total_priests': total_dio_priests+total_order_priests,
    }
    return render(request, 'diocese/orderview.html', context)



def alpha_orderpriestlist(request):
    alphabet = string.ascii_uppercase
    context = {'alphabet': alphabet}
    return render(request, 'diocese/orderalphapriest_list.html', context)


def alpha_priestlist(request):
    alphabet = string.ascii_uppercase
    context = {'alphabet': alphabet}
    return render(request, 'diocese/alphapriest_list.html', context)

def priest(request):
    table = PriestTable(Priest.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'diocese/priest_list.html', {'table': table})


def nun(request):
    table = PriestTable(Priest.objects.all().filter(clergy_type="N"))
    RequestConfig(request).configure(table)
    return render(request, 'diocese/nun_list.html', {'table': table})



def orderpriestlist_view(request, letter=None):
    table = OrderPriestTable(Priest.objects.all().filter(order_priest=True, last_name__startswith=letter))
    RequestConfig(request).configure(table)
    return render(request, 'diocese/orderpriest_list.html', {'table': table})


def priestlist_view(request, letter=None):
    table = PriestTable(Priest.objects.all().filter(order_priest=False, last_name__startswith=letter))
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
        return ( {'exclude': ('id','year_born','order_name','order_priest','offender','clergy_type',)}
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

  
class OrderPriestListView(DetailView):
    model = Priest
    template_name = "diocese/order_priest_list.html"

    def get_object(self):
        """Returns the Archdiocese instance that the view displays"""
        return get_object_or_404(Order, pk=self.kwargs.get("pk"))
