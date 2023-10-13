from django.contrib import admin
from app.models.delivery import (
    Customer,
    PurchaseDetail,
    PurchaseOrder,
    SaleDetail,
    SaleOrder,
    Supplier,
    InvoiceFile
)
from app.models.storage import (
    Brand,
    Category,
    Inventory,
    InventoryReport,
    Product,
    ProductVariant,
    Property,
    Warehouse,
    Warranty,
    ProductImage,
)

from app.models.user import User

# Register your models here.


# Category Admin
# ----------------------------------------------------------------
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


# Brand Admin
# ----------------------------------------------------------------
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


# Warehouse Admin
# ----------------------------------------------------------------
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


# Product Admin
# ----------------------------------------------------------------
class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant

class PropertiesInline(admin.TabularInline):
    model = Property


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "sku"]
    inlines = [ProductImageInline, ProductVariantInline, PropertiesInline]


# Warranty Admin
# ----------------------------------------------------------------
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


# Inventory Admin
# ----------------------------------------------------------------
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["variant", "id", "warehouse", "quantity"]
    list_filter = ["warehouse"]
    search_fields = ["variant__name"]

class InventoryReportAdmin(admin.ModelAdmin):
    list_display = ["inventory", "onhand_date"]


# User Admin
# ----------------------------------------------------------------
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["user_name", "id"]


# Supplier Admin
# ----------------------------------------------------------------
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "id"]


# Customer Admin
# ----------------------------------------------------------------
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "id"]


# Invoice Admin
# ----------------------------------------------------------------
class InvoiceInline(admin.TabularInline):
    model = InvoiceFile

# Purchase Admin
# ----------------------------------------------------------------
class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["sku", "id"]
    list_filter = ["created_at", "total_amount"]
    inlines = [PurchaseDetailInline, InvoiceInline]


class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ["product", "id"]


# Sale Order Admin
# ----------------------------------------------------------------
class SaleDetailInline(admin.TabularInline):
    model = SaleDetail
    raw_id_fields = ["variant"]


class SaleAdmin(admin.ModelAdmin):
    model = SaleOrder
    list_display = ["sku", "id"]
    inlines = [SaleDetailInline]
    list_filter = ["created_at", "total_amount"]


class SaleDetailAdmin(admin.ModelAdmin):
    model = SaleDetail
    list_display = ["variant", "id"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(PurchaseOrder, PurchaseAdmin)
admin.site.register(SaleOrder, SaleAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryReport, InventoryReportAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
