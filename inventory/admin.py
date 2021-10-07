from django.contrib import admin

from .models import itemFlavor, sizeCounts

admin.site.register(itemFlavor, sizeCounts)

# Register your models here.
