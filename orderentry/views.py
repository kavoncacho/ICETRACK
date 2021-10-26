from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import orderentry
from orderentry.forms import customerForm

def getCustomerInfo(request):
    form = customerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.customer_first_name = form.cleaned_data['customer_first_name']
            orderentry.forms.customer_last_name = form.cleaned_data['customer_last_name']
            orderentry.forms.shipping_address = form.cleaned_data['shipping_address']
            orderentry.forms.billing_address = form.cleaned_data['billing_address']
            return redirect('/orderentry')

    else:
        form=customerForm()
    
    return render(request, 'orderentry.html', {'form' : form})

