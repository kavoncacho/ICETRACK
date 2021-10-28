from django.contrib import admin

from ticketmanage.models import externalTicket, internalTicket

# Register your models here.
admin.site.register(internalTicket)
admin.site.register(externalTicket)