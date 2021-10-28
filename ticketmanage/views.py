from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import ticketmanage
from ticketmanage.forms import ticketForm

from ticketmanage.forms import ticketForm

def getTicketInfo(request):
    form = ticketForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            ticketmanage.user_name = form.cleaned_data['user_name']
            ticketmanage.user_email = form.cleaned_data['user_email']
            ticketmanage.ticket_creation_date = form.cleaned_data['ticket_creation_date']
            ticketmanage.subject = form.cleaned_data['subject']
            ticketmanage.description = form.cleaned_data['description']

            return redirect('sorry')

    else:
        form=ticketForm()
    
    return render(request, 'ticketmanage.html', {'form' : form})

def sorry(request):
    return render(request, 'sorry.html')