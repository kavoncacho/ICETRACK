from django import forms
from shipmenttracking.models import shipmentTrack

class shipmentTrackForm (forms.Form):
    
    trackingCode = forms.IntegerField()