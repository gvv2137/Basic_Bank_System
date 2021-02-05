from django.shortcuts import render
from TSF_Bank.models import Customer
from TSF_Bank.models import Transaction

# Create your views here.
def home(request):
    return render(request,'TSF_Bank/index.html')

def custview(request):
    cust_list=Customer.objects.all()
    my_dict={'cust_list':cust_list}
    return render(request,'TSF_Bank/customers.html',context=my_dict)

def transactions(request):
    data = Transaction.objects.all()
    my_dict = {"transactions": data}
    return render(request, "TSF_Bank/transactions.html", context=my_dict)

def send(request):
    if request.method == "POST":
        acnoself = request.POST["acnoself"]
        acno = request.POST["acno"]
        name = request.POST["name"]
        amount = request.POST["amount"]
        try:
            receiver = Customer.objects.get(account_number=acno)
            sender = Customer.objects.get(account_number=acnoself)
            amount = int(amount)
            if name == receiver.ename:
                if amount <= sender.account_balance:
                    print(sender.account_balance, receiver.account_balance)
                    sender.account_balance -= amount
                    receiver.account_balance += amount
                    print(sender.account_balance, receiver.account_balance)
                    sender.save()
                    receiver.save()
                    new_txn = Transaction(
                        debited_from=sender, credited_to=receiver, amount=amount)
                    new_txn.save()
                    return render(request,"TSF_Bank/send.html", {"message": "Transaction successful."})
                else:
                    return render(request, "TSF_Bank/send.html", {"error": "Your account doesn't have sufficient balance."})
            else:
                return render(request, "TSF_Bank/send.html", {"error": "Please enter correct details."})
        except Customer.DoesNotExist:
            return render(request, "TSF_Bank/send.html", {"error": "Account Number does not match with any customer."})
    else:
        return render(request, "TSF_Bank/send.html") 