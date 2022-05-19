from django.contrib import admin
from .models import Client, Service, Payment

# Register your models here.


admin.site.site_header = 'Resort Management System'
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name','mobilenumber','address','amount','datetime']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','mobilenumber','idproof','proof','address']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['services', 'name', 'mobilenumber', 'idproof', 'proof', 'address', 'amount', 'datetime']


admin.site.register(Client,ClientAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Payment,PaymentAdmin)