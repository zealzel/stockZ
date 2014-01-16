from django.contrib import admin

# Register your models here.
from financial.models import Prices

class PriceAdmin(admin.ModelAdmin):
    list_display=('date','p_max','p_min','p_end')
    
admin.site.register(Prices, PriceAdmin)