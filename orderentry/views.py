from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import orderentry
from orderentry.forms import customerForm, customerInformation

def getCustomerInfo(request):
    form = customerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.customer_first_name = form.cleaned_data['customer_first_name']
            orderentry.forms.customer_last_name = form.cleaned_data['customer_last_name']
            orderentry.forms.shipping_address = form.cleaned_data['shipping_address']
            orderentry.forms.billing_address = form.cleaned_data['billing_address']
            return redirect('thankyou')

    else:
        newOrder=customerInformation()
        form=customerForm()
    
    return render(request, 'orderentry.html', {'form' : form, "newOrder": newOrder})

def getCustomerOrder(request):
    newOrder = customerInformation(request.POST)
    if request.method == 'POST':
        if newOrder.is_valid():
            newOrder.save()
            orderentry.forms.order_Item_Flavor = newOrder.cleaned_data['order_Item_Flavor']
            orderentry.forms.half_Pint_Count = newOrder.cleaned_data['half_Pint_Count']
            orderentry.forms.one_Quart_Count = newOrder.cleaned_data['one_Quart_Count']
            orderentry.forms.pint_Count = newOrder.cleaned_data['pint_Count']
            orderentry.forms.half_Gallon_Count = newOrder.cleaned_data['half_Gallon_Count']
            orderentry.forms.gallon_Count = newOrder.cleaned_data['gallon_Count']
            orderentry.forms.cost = newOrder.cleaned_data['cost']
            return redirect('thankyou')
    else:
        newOrder=customerInformation()
    
    return render(request, 'orderentry.html', {'newOrder' : newOrder})

def thankYou(request):
    return render(request, 'thankyou.html')