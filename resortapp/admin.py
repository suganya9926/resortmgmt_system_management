from django.contrib import admin
from .models import Client, Service, Payment,ServiceAdmin,PaymentAdmin

# Register your models here.
admin.site.site_header = 'Resort Management System'

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobilenumber', 'idproof', 'proof', 'address']


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Payment, PaymentAdmin)
