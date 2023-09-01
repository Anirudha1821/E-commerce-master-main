from django.contrib import admin
from .models import Products,Contact,Merchant

# Register your models here.
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Merchant)

# here we cak also use 
# to register 

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display=['id','name','roll','city']

# here id is self incremented 
    