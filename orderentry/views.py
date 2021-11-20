from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import orderentry
from orderentry.forms import customerInfo, customerOrder

def getCustomerOrder(request):
    form = customerOrder(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.order_Item_Flavor = form.cleaned_data['order_Item_Flavor']
            orderentry.forms.half_Pint_Count = form.cleaned_data['half_Pint_Count']
            orderentry.forms.one_Quart_Count = form.cleaned_data['one_Quart_Count']
            orderentry.forms.pint_Count = form.cleaned_data['pint_Count']
            orderentry.forms.half_Gallon_Count = form.cleaned_data['half_Gallon_Count']
            orderentry.forms.gallon_Count = form.cleaned_data['gallon_Count']
            return redirect('continueOrder')
    else:
        form=customerOrder()
    
    return render(request, 'orderentry.html', {'form' : form})

def getCustomerInfo(request):
    form = customerInfo(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.customer_first_name = form.cleaned_data['customer_first_name']
            orderentry.forms.customer_last_name = form.cleaned_data['customer_last_name']
            orderentry.forms.shipping_address = form.cleaned_data['shipping_address']
            orderentry.forms.billing_address = form.cleaned_data['billing_address']
            return redirect('thankyou')

    else:
        form=customerInfo()
    
    return render(request, 'customerinfoentry.html', {'form' : form})

def thankYou(request):
    return render(request, 'thankyou.html')

def continueOrder(request):
    return render(request, 'customerinfoentry.html')