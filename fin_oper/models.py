from django.db import models

# Create your models here.
class Sale(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_sale = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.id

class Purchase(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_purchase = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.id

class TypeTransaction(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    type_transaction = models.OneToOneField(TypeTransaction, on_delete=models.PROTECT)
    date_transaction = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.id

