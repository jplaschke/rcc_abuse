from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from diocese.models.diocese_model import Archdiocese
from diocese.models.diocese_model import Diocese

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