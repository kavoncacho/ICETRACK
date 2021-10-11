from django.contrib import admin

from orderentry.models import customerInfo, invoice, orderInfo

admin.site.register(invoice)
admin.site.register(customerInfo)
admin.site.register(orderInfo)

# Register your models here.
