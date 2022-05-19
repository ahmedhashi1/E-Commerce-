from django.contrib import admin
from .models import Products,Order
# Register your models here.


admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','discount_price','category','description')
    search_fields = ('name',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)