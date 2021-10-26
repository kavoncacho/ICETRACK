from django.shortcuts import render
from django.http import HttpResponse
from .forms import customer_Information
from django.views.generic import TemplateView

class OrderEntryView(TemplateView):
    template_name = 'orderentry/templates/orderentry.html'

    def get(self, request):
        form = customer_Information()

        return render(request, 'self.template_name', {'form': form} )
 
#def get_customer_info(request):

    #if request.method == 'POST':
     #   form = customer_Information(request.POST)
      #  if form.is_valid():

    #return render(request, 'orderentry.html')
