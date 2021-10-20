from django.contrib import admin

from .models import item, sizeCounts

admin.site.register(item)
admin.site.register(sizeCounts)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','flavor','size quantities')

# Register your models here.
