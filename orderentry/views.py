from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import customer_Information

class OrderEntryView(TemplateView):
    template_name = 'orderentry.html'

    def get(self, request):
        form = customer_Information()
        return render(request, self.template_name, {"forms": form})

    def post(self, request):
        form = customer_Information(request.POST)
        firstName = None
        lastName = None
        shipAddr = None
        billAddr = None
        if form.is_valid():
            
            form.save()

            firstName = form.cleaned_data["customerFirstName"]
            lastName = form.cleaned_data["customerLastName"]
            shipAddr = form.cleaned_data["ShippingAddress"]
            billAddr = form.cleaned_data["BillingAddress"]
            form = customer_Information()
            
            return redirect('orderentry:orderentry')
        else:
            print(form.errors)

        args = {"forms": form, "firstName": firstName, "lastName": lastName, "shipAddr": shipAddr, "billAddr": billAddr}
        
        return render(request, self.template_name, args)



