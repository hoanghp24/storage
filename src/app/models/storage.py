from django.db import models

#helpers
from app.helpers.location_file import location_img, location_barcode_img, location_qrcode_img

#models
from app.models.base import BaseModel, TERMTYPE

# Create your models here.

# Warranty Terms: Thời hạn bảo hành
# ----------------------------------------------------------------
class Warranty(BaseModel):
    name = models.CharField(max_length=255)
    term_number = models.IntegerField()
    term_type = models.CharField(max_length=20, choices=TERMTYPE.CHOICES)

    class Meta:
        verbose_name_plural = "Thời hạn bảo hành"

    def __str__(self):
        return self.name

# Category: Nhóm hàng
# ----------------------------------------------------------------
class Category(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, 
        related_name="children"
    )

    @property
    def children(self):
        return self.get_children()

    @property
    def ancestors(self):
        return self.parent

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Loại sản phẩm"

# Brand: Thương hiệu
# ----------------------------------------------------------------
class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Nhãn hiệu"

# Warehouse: Vị trí lưu kho
# ----------------------------------------------------------------
class Warehouse(BaseModel):
    sku = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Chi nhánh"

    def __str__(self):
        return self.name
    
# Product: Hàng hoá
# ----------------------------------------------------------------
class Product(BaseModel):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, null=True, unique=True)
    qrcode = models.ImageField(upload_to=location_qrcode_img, null=True, blank=True)
    image = models.ImageField(upload_to=location_img, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    warranty = models.ForeignKey(Warranty, on_delete=models.SET_NULL, null=True)
    unit = models.JSONField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Sản phẩm"

    def __str__(self):
        return "{} - {}".format(self.sku, self.name)
  
# Product Variant: Phiên bản hàng hoá 
# ------------------------------------------------------------------
class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    sku = models.CharField(max_length=100, null=True, unique=True)
    barcode = models.CharField(max_length=100, null=True, unique=True)
    barcode_image = models.ImageField(upload_to=location_barcode_img, null=True, blank=True)
    price = models.CharField(max_length=100, blank=True) # Giá bán
    cost = models.CharField(max_length=100, blank=True) # Giá nhập
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)  
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ("company_id", "sku")
        verbose_name_plural = "Phiên bản sản phẩm"

    def __str__(self):
        return "{} - {} - {}".format(self.sku, self.name, self.quantity)
    
# Product Images
# ----------------------------------------------------------------
class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to=location_img, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name_plural = "Ảnh sản phẩm"
    
# Properties: Thuộc tính
# ----------------------------------------------------------------
class Property(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=100)
    value = models.JSONField()
    position = models.IntegerField()
    is_edited = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Thuộc tính"

# Inventory: Tồn kho
# ----------------------------------------------------------------
class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="inventories")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.variant.name
    
    class Meta:
        verbose_name_plural = "Tồn kho"
    
class InventoryReport(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    inventory = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)
    inventory_data = models.JSONField(null=True, blank=True)
    onhand_date = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        verbose_name_plural = "Báo cáo"