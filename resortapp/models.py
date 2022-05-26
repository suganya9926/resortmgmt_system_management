from django.contrib import admin
from django.db import models
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=30)
    mobilenumber = models.CharField(max_length=30)
    myidproof = [('Aadhaar Card', 'Aadhaar Card'), ('Passport', 'Passport'), ('Driving Licence', 'Driving Licence'),
                 ('Voter ID', 'Voter ID'), ('Pan Card', 'Pan Card')]
    idproof = models.CharField(choices=myidproof, max_length=30)
    proof = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30)


class Service(models.Model):
    myservices = [('Single bedroom', 'Single bedroom'), ('Double bedroom', 'Double bedroom'),
                  ('VIP bedroom', 'VIP bedroom'), ('Car parking', 'Car parking'), ('Eclectic food', 'Eclectic food'),
                  ('Room services', 'Room services')]
    services = models.CharField(choices=myservices, max_length=30,null=True)
    name = models.CharField(max_length=30, null=True)
    mobilenumber = models.CharField(max_length=10, null=True)
    myidproof = [('Aadhaar Card', 'Aadhaar Card'), ('Passport', 'Passport'), ('Driving Licence', 'Driving Licence'),
                 ('Voter ID', 'Voter ID'), ('Pan Card', 'Pan Card')]
    idproof = models.CharField(choices=myidproof, max_length=30, null=True)
    proof = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    car_number = models.CharField(max_length=30,null=True)
    mychoices = [('South Indian', 'South Indian'), ('North Indian', 'North Indian'), ('Chinese', 'Chinese'),
                 ('Italian', 'Italian'),
                 ('Pan Asian', 'Pan Asian'), ('European', 'European'), ('Japanese', 'Japanese'),
                 ('Casual Electic', 'Casual Electic'),
                 ('Meditterranean', 'Meditterranean')]
    choices = models.CharField(choices=mychoices, max_length=30,null=True)
    myfavors = [('Centralized', 'Centralized'), ('Decentralized', 'Decentralized')]
    favors = models.CharField(choices=myfavors, max_length=30,null=True)
    count = models.IntegerField(default=1)
    amount = models.IntegerField(default=6000)

    now = datetime.now()

    def mydatetime(self):
        return self.now.strftime("%d-%m-%Y, %H:%M:%S")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['services', 'name', 'mobilenumber', 'idproof', 'proof', 'address', 'car_number', 'choices', 'favors','amount', 'count', 'mydatetime']


class Singlebedroom(models.Model):
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    count = models.IntegerField()
    amount = models.IntegerField(default=6000)

    def __str__(self):
        return f'{self.services}-{self.count}-{self.amount}'


class Doublebedroom(models.Model):
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    count = models.IntegerField()
    amount = models.IntegerField(default=8000)

    def __str__(self):
        return f'{self.services}-{self.count}-{self.amount}'


class VIPbedroom(models.Model):
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    count = models.IntegerField()
    amount = models.IntegerField(default=10000)

    def __str__(self):
        return f'{self.services}-{self.count}-{self.amount}'


class Carparking(models.Model):
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    car_number = models.CharField(max_length=30)
    amount = models.IntegerField(default=2000)

    def __str__(self):
        return f'{self.services}-{self.car_number}-{self.amount}'


class Eclecticfood(models.Model):
    mychoices = [('South Indian', 'South Indian'), ('North Indian', 'North Indian'), ('Chinese', 'Chinese'),
                 ('Italian', 'Italian'),
                 ('Pan Asian', 'Pan Asian'), ('European', 'European'), ('Japanese', 'Japanese'),
                 ('Casual Electic', 'Casual Electic'),
                 ('Meditterranean', 'Meditterranean')]
    choices = models.CharField(choices=mychoices, max_length=30)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=6000)

    def __str__(self):
        return f'{self.choices}-{self.services}-{self.amount}'


class Roomservices(models.Model):
    myfavors = [('Centralized', 'Centralized'), ('Decentralized', 'Decentralized')]
    favors = models.CharField(choices=myfavors, max_length=30)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=4000)

    def __str__(self):
        return f'{self.favors}-{self.services}-{self.amount}'


class Payment(models.Model):
    mypayouts = [('Bank Account', 'Bank Account'), ('Google pay', 'Google pay'), ('Paytm', 'Paytm'),
                 ('Phonepe', 'Phonepe'),
                 ('Paypal', 'Paypal'), ('Credit Card', 'Credit_Card'), ('Credit Card', 'Credit Card'), ('Cash', 'Cash')]
    payouts = models.CharField(choices=mypayouts, max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    mobilenumber = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    account_number = models.CharField(max_length=30, null=True)
    UPI_id = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    credit_card_number = models.CharField(max_length=30, null=True)
    debit_card_number = models.CharField(max_length=30,null=True)
    amount = models.IntegerField(default=25000)

    now = datetime.now()

    def mydatetime(self):
        return self.now.strftime("%d-%m-%Y, %H:%M:%S")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobilenumber', 'address', 'account_number', 'UPI_id', 'email', 'credit_card_number', 'debit_card_number', 'amount', 'mydatetime']



class Bankaccount(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Googlepay(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Paytm(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Phonepe(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Paypal(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Creditcard(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)


class Debitcard(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

class Cash(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

