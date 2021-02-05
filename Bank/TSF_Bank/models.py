from django.db import models

# Create your models here.
class Customer(models.Model):
    ename=models.CharField(max_length=30)
    email= models.EmailField(unique=True)
    account_number= models.CharField(max_length=255, unique=True)
    account_balance= models.IntegerField(default=0)
    def __str__(self):
        return self.ename

class Transaction(models.Model):
    debited_from = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="sender")
    credited_to = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="receiver")
    amount = models.IntegerField(default=0)