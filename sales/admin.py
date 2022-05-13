from django.contrib import admin
from sales.models import sales
# Register your models here.

# class farmeradmin(admin.ModelAdmin):
#     list_display=['farmer_id','farmer_name','adhaar_no','phone_no','photo','address']
#admin.site.register(farmer)

#admin.site.register(farmer)
# class productadmin(admin.ModelAdmin):
#     list_display=['product_id','product_name','product_img','quantity','price','farmer_id','manager_id']
#admin.site.register(product)
#admin.site.register(manager)
#admin.site.register(inventory)
#admin.site.register(stocks)
admin.site.register(sales)