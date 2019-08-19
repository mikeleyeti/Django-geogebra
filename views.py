from django.shortcuts import render,get_object_or_404
from .models import Geogebra


def index(request):
    geogebra_list = Geogebra.objects.all()
    context = {
        'geogebra_list' : geogebra_list
    }
    return render(request, 'geogebra/index.html', context)
