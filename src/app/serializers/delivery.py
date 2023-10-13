# django restframework
from django.conf import settings
from rest_framework import serializers

# models
from app.models.delivery import (
    Customer,
    InvoiceFile, 
    PurchaseOrder, 
    SaleDetail, 
    SaleOrder, 
    Supplier, 
    PurchaseDetail
)

#serializers
from app.serializers.storage import ProductVariantSerializer, WarehouseSerializer


# Create your serializers here.

# Supplier Serializer
#----------------------------------------------------------------
class CreateSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name", "email", "phone", "address"]

    def create(self, validated_data):
        supplier = Supplier.objects.create(**validated_data)
        supplier.sku = f"SUP{str(supplier.id).zfill(5)}"
        supplier.save()
        return supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

# Customer Serializer
#----------------------------------------------------------------
class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone", "address"]

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        customer.sku = f"CUS{str(customer.id).zfill(5)}"
        customer.save()
        return customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

# Purchase Order Serializer
# ------------------------------------------------------------------------------
class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = ["variant", "name", "discount", "unit", "cost", "quantity", "subtotal"]
        extra_kwargs = {
            "purchase": {"write_only": True},
        }

    def create(self, validated_data):
        purchase_detail = PurchaseDetail(**validated_data)
        purchase_detail.save()
        return purchase_detail
    
    def to_representation(self, instance):
        self.fields["variant"] = ProductVariantSerializer(read_only=True)
        return super(PurchaseDetailSerializer, self).to_representation(instance)

class CreatePurchaseOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrder
        fields = [
            "user_id", "supplier", "warehouse", "note",
            "payment_method", "purchase_details", "discount_amount", "total_quantity", "total_amount"
        ]

    def create(self, validated_data):
        purchase = PurchaseOrder.objects.create(**validated_data)
        purchase.sku = f"PON{str(purchase.id).zfill(5)}"
        purchase.save()
        
        return purchase
    
class UpdatePurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["user_id", "supplier", "warehouse", "note", 'invoice'] 


class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_details = PurchaseDetailSerializer(many=True)
    supplier = SupplierSerializer()
    warehouse = WarehouseSerializer()
    invoices = serializers.SerializerMethodField('get_invoice')
    class Meta:
        model = PurchaseOrder
        fields = ["id", "company_id", "sku", "purchase_details", "supplier", "invoices", "note", "payment_method",
                  "discount_amount", "total_quantity", "total_amount", "warehouse", "user_id", "created_at", "updated_at"]
    
    def get_invoice(self, obj):
        return [f"{settings.HOST_URL}{invoice.invoice.url}" for invoice in obj.invoices.all()]


# Sale Order Serializer
# ------------------------------------------------------------------------------
class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ["variant", "name", "discount", "unit", "price", "quantity", "subtotal"]
        extra_kwargs = {
            "order": {"write_only": True},
        }

    def create(self, validated_data):
        sale_detail = SaleDetail(**validated_data)
        sale_detail.save()
        return sale_detail
    
    def to_representation(self, instance):
        self.fields["variant"] = ProductVariantSerializer(read_only=True)
        return super(SaleDetailSerializer, self).to_representation(instance)

class CreateSaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = [
            "user_id", "customer", "note", "warehouse", "payment_method", 
            "sale_details", "discount_amount", "total_quantity", "total_amount"
        ]

    def create(self, validated_data):
        order = SaleOrder.objects.create(**validated_data)
        order.sku = f"SON{str(order.id).zfill(5)}"
        order.save()
        return order
    
class UpdateSaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ["user_id", "customer", "note", "invoice"] 

class SaleOrderSerializer(serializers.ModelSerializer):
    sale_details = SaleDetailSerializer(many=True)
    customer = CustomerSerializer()
    warehouse = WarehouseSerializer()
    invoices = serializers.SerializerMethodField('get_invoice')
    class Meta:
        model = SaleOrder
        fields = ["id", "company_id", "sku", "sale_details", "customer", "invoices", "note", "payment_method",
                  "discount_amount", "total_quantity", "total_amount", "warehouse", "user_id", "created_at", "updated_at"]
    
    def get_invoice(self, obj):
        return [f"{settings.HOST_URL}{invoice.invoice.url}" for invoice in obj.invoices.all()]