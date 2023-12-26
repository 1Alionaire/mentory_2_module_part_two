from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    hobby = models.TextField()
    previous_work_place = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + self.last_name

class PreferenceBrand(models.Model):
    client_id = models.ForeignKey(to=Client(id), on_delete=models.PROTECT)
    prefer_brand_name = models.CharField(max_length=20)
    prefer_brand_description = models.TextField()

    def __str__(self):
        return self.prefer_brand_name

class PreferenceCategory(models.Model):
    client_id = models.ForeignKey(to=Client(id), on_delete=models.PROTECT)
    prefer_category_name = models.CharField(max_length=20)
    prefer_category_description = models.TextField()

    def __str__(self):
        return self.prefer_category_name


