from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from diocese.models.diocese_model import Archdiocese
from diocese.models.diocese_model import Diocese
from diocese.models.diocese_model import Priest

def index(request):
    archdiocese_list = Archdiocese.objects.order_by('name')
    context = {
        'archdiocese_list': archdiocese_list,
    }
    return render(request, 'diocese/index.html', context)


class DioceseDetailView(DetailView):
    model = Archdiocese

    def get_object(self):
        """Returns the Archdiocese instance that the view displays"""
        return get_object_or_404(Archdiocese, pk=self.kwargs.get("pk"))

class PriestList(ListView):
    model = Priest
    queryset = Priest.objects.all()
    context_object_name = 'priest_list'
  
  
  
class PriestDetailView(DetailView):
    model = Priest

    def get_object(self):
        """Returns the Diocese instance that the view displays"""
        return get_object_or_404(Diocese, pk=self.kwargs.get("pk"))