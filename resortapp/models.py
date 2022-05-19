from django.db import models
import datetime


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    mobilenumber = models.CharField(max_length=30)
    myidproof = [('Aadhaar Card', 'Aadhaar Card'), ('Passport', 'Passport'), ('Driving Licence', 'Driving Licence'),
                 ('Voter ID', 'Voter ID'), ('Pan Card', 'Pan Card')]
    idproof = models.CharField(choices=myidproof, max_length=30)
    proof = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30)

    # def __str__(self):
    #     return f'{self.name}-{self.mobilenumber}-{self.idproof}-{self.address}'


class Service(models.Model):
    myservices = [('Single bedroom', 'Single bedroom'), ('Double bedroom', 'Double bedroom'),
                  ('VIP bedroom', 'VIP bedroom'), ('Car parking', 'Car parking'), ('Eclectic food', 'Eclectic food'),
                  ('Room services', 'Room services')]
    services = models.CharField(choices=myservices, max_length=30)
    name = models.CharField(max_length=30, null=True)
    mobilenumber = models.CharField(max_length=30, null=True)
    myidproof = [('Aadhaar Card', 'Aadhaar Card'), ('Passport', 'Passport'), ('Driving Licence', 'Driving Licence'),
                 ('Voter ID', 'Voter ID'), ('Pan Card', 'Pan Card')]
    idproof = models.CharField(choices=myidproof, max_length=30, null=True)
    proof = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    amount = models.IntegerField(default=6000)

    sdate=datetime.datetime.now()
    newdate=sdate.strftime('%d-%m-%Y')
    mydate=datetime.datetime.strptime(newdate,'%d-%m-%Y')
    datetime = models.DateTimeField(default=mydate)

    # def __str__(self): return f'{self.services}-{self.name}-{self.mobilenumber}-{self.idproof}-{self.proof}-{
    # self.address}-{self.amount}-' \ f'{self.datetime} '


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
    payouts = models.CharField(choices=mypayouts, max_length=30)
    name = models.CharField(max_length=30)
    mobilenumber = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    amount = models.IntegerField(default=25000)
    datetime = models.DateTimeField(null=True)

    # def __str__(self):
    #     return f'{self.name}-{self.mobilenumber}-{self.payouts}-{self.amount}-{self.datetime}'


class Bankaccount(models.Model):
    account_number = models.CharField(max_length=30)
    IFC_code = models.CharField(max_length=30)
    Bank_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.account_number}-{self.IFC_code}-{self.Bank_name}'


class Googlepay(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    UPI_id = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.payments}-{self.UPI_id}'


class Paytm(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    UPI_id = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.payments}-{self.UPI_id}'


class Phonepe(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    UPI_id = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.payments}-{self.UPI_id}'


class Paypal(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.payments}-{self.email}'


class Creditcard(models.Model):
    MMID = models.CharField(max_length=30)
    mobilenumber = models.CharField(max_length=30)
    credit_card_number = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.MMID}-{self.mobilenumber}-{self.credit_card_number}'


class Debitcard(models.Model):
    debit_card_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.debit_card_number}-{self.address}'


class Cash(models.Model):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.payments}'
