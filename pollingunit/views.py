from unittest import result
from django.shortcuts import render
from .models import AnnouncedPuResults, Lga, PollingUnit


# Create your views here.
def index(request):
    if request.method == 'POST':
        value = int(request.POST.get("search"))
        pu_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=value)
        context = {
            'pu_results': pu_results,
            'value': value
        }
        return render(request, "index.html", context)
    return render(request, "index.html")

def polling_unit(request):
    polling_unit = PollingUnit.objects.all()
    context = {
        'polling_unit': polling_unit
    }
    return render(request, "pollingunit.html", context)

def local_government(request):
    lga = Lga.objects.all()
    context = {
        'lga': lga
    }
    return render(request, "localgovernment.html", context)

