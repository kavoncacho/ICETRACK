from django.shortcuts import render
from django.http import HttpResponse
import shipmenttracking
from shipmenttracking.forms import shipmentTrackForm 

def getShipmentCode(request):
    form = shipmentTrackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            shipmenttracking.forms.trackingCode = form.cleaned_data['trackingCode']
    else:
        form = shipmentTrackForm()
    
    return render(request, 'shipmenttracking.html', {'form' : form})