from django.shortcuts import render
from django.http import HttpResponse
from .models import customerInfo, orderInfo, invoice
from inventory.models import sizeCounts, item

def index(request):

    return render(request, 'orderentry.html')
