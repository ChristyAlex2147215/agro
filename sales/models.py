from django.db import models
from manager.models import manager
from customer.models import customer

# Create your models here.
class sales(models.Model):
    sales_id=models.CharField(max_length=20)
    quantity_in_kg=models.IntegerField()
    stock_name=models.CharField(max_length=20)
    price_per_kg=models.IntegerField()
    #customer_id=models.ForeignKey(customer(), on_delete=models.CASCADE)
    #manager_id=models.ForeignKey(manager(), on_delete=models.CASCADE)
    
    
# class stocks(models.Model):
#     stock_id=models.IntegerField(primary_key=True)
#     stock_name=models.CharField(max_length=20)
#     available_quantity=models.FloatField()
#     price=models.FloatField()
#     inventory_id=models.ForeignKey(inventory, on_delete=models.CASCADE)
#     product_id=models.ForeignKey(product, on_delete=models.CASCADE)    
