from django.contrib import admin
from TSF_Bank.models import Customer
from TSF_Bank.models import Transaction
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['ename','email','account_number','account_balance']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['debited_from', 'credited_to', 'amount']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Transaction,TransactionAdmin)

admin.site.site_header = 'Bank Admin Panel'