from django.contrib import admin

from orderentry.models import customerInfo, orderInfo

admin.site.register(customerInfo)
admin.site.register(orderInfo)

# Register your models here.
