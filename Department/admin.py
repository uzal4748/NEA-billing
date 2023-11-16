from django.contrib import admin
from Department.models import Branch, Payment, PaymentOption, Demandtype, Customer, Demandrate, Bill
# Register your models here.
admin.site.register(Branch)
admin.site.register(PaymentOption)
admin.site.register(Demandtype)
admin.site.register(Customer)
admin.site.register(Demandrate)
admin.site.register(Bill)
admin.site.register(Payment)