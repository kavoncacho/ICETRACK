from django.contrib import admin

from .models import item, sizeCounts, flavor, prices

admin.site.register(item)
admin.site.register(flavor)
admin.site.register(sizeCounts)
admin.site.register(prices)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','flavor','size quantities')

# Register your models here.
