from django.db import models

# Create your models here.
class customer(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=80)