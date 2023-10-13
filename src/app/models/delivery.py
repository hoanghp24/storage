from django.db import models

#helpers
from app.helpers.location_file import location_file

#models
from app.models.storage import  ProductVariant, Warehouse, Product
from app.models.base import BaseModel


# Create your models here.

#Supplier: Nhà cung cấp
#----------------------------------------------------------------
class Supplier(BaseModel):
    sku = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    metadata = models.JSONField(null=True, blank=True)


    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Nhà cung cấp"
    
    def __str__(self):
        return self.name

#Customer: Khách hàng
#----------------------------------------------------------------
class Customer(BaseModel):
    sku = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Khách hàng"

    def __str__(self):
        return self.name
    
#PurchaseOrder: Nhập hàng|Mua hàng
#----------------------------------------------------------------
class PurchaseOrder(BaseModel):
    user_id = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=100, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    note = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50) 
    discount_amount = models.FloatField(default=0)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0)

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Nhập hàng"

    def __str__(self):
        return self.sku

    @property
    def purchase_details(self):
        return self.purchasedetail_set.all()
    
class PurchaseDetail(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    purchase =  models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    cost = models.CharField(max_length=100, null=True)
    discount = models.IntegerField(default=0, null=True)
    unit = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=0)
    subtotal = models.CharField(max_length=100, null=True) 

#SaleOrder: Xuất hàng|Bán hàng
#--------------------------------------------------------
class SaleOrder(BaseModel):
    user_id = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    note = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50) 
    discount_amount = models.FloatField(default=0)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0)

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Đơn hàng"

    def __str__(self):
        return self.sku

    @property
    def sale_details(self):
        return self.saledetail_set.all()

class SaleDetail(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    order =  models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=100, null=True)
    discount = models.IntegerField(default=0, null=True)
    unit = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=0)
    subtotal = models.CharField(max_length=100, null=True) 


#InvoiceFile: Chứng từ
#--------------------------------------------------------
class InvoiceFile(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    invoice = models.FileField(upload_to=location_file, null=True, blank=True)
    purchase = models.ForeignKey(PurchaseOrder, on_delete=models.SET_NULL, null=True, related_name = "invoices")
    order = models.ForeignKey(SaleOrder, on_delete=models.SET_NULL, null=True, related_name = "invoices")
