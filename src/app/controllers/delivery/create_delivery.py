#django restframework
from rest_framework.decorators import api_view
from django.db import transaction
import json
from app.models.delivery import InvoiceFile

#models
from app.models.storage import Inventory, ProductVariant

#serializers
from app.serializers.delivery import (
    CreateCustomerSerializer,
    CustomerSerializer,
    PurchaseOrderSerializer,
    PurchaseDetailSerializer,
    CreatePurchaseOrderSerializer,
    SaleDetailSerializer, 
    CreateSaleOrderSerializer,
    SaleOrderSerializer,
    SupplierSerializer,
    CreateSupplierSerializer
)

#helpers
from app.helpers.response import BadRequest, CreateSuccess, ServerError
from app.helpers.common_business import get_data

# Create your API here.

# Supplier API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_supplier(request):
    try:
        data = get_data(request)
        serializer = CreateSupplierSerializer(data=request.data)
        if serializer.is_valid():
            supplier = serializer.save(company_id=data["company_id"])
            serializer = SupplierSerializer(supplier)
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()

# Customer API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_customer(request):
    try:
        data = get_data(request)
        serializer = CreateCustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save(company_id=data["company_id"])
            serializer = CustomerSerializer(customer)
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except Exception as e:
        return ServerError(str(e))

#Purchase Order API
#----------------------------------------------------------------
@api_view(['POST'])
def create_purchase_order(request):
    try:
        with transaction.atomic():
            data = get_data(request, is_form_data=True)
            purchase_details = json.loads(data["purchase_details"])
            invoices = request.FILES.getlist("invoices")
            warehouse = data["warehouse"]
            #Purchase Order
            purchase_seria = CreatePurchaseOrderSerializer(data=data)
            if not purchase_seria.is_valid():
                return BadRequest(purchase_seria.errors)
            purchase = purchase_seria.save(company_id=data['company_id'])
            #Purchase Order Details
            purchase_detail_seria = PurchaseDetailSerializer(data=purchase_details, many=True)
            if not purchase_detail_seria.is_valid():
                return BadRequest(purchase_detail_seria.errors)
            purchase_detail_seria.save(purchase=purchase)
            #Update Product Variant
            for detail in purchase_details:
                variant = ProductVariant.objects.get(company_id=data['company_id'], id=detail['variant'])
                variant.quantity += detail['quantity']
                variant.save() 
                #Update Inventory
                inventories = Inventory.objects.filter(company_id=data['company_id'], variant=variant, warehouse_id=warehouse).first()
                inventories.quantity += detail['quantity']
                inventories.save()
            #Invoices
            for invoice in invoices:
                InvoiceFile.objects.create(company_id=purchase.company_id, purchase=purchase, invoice=invoice)
            
            purchase_seria = PurchaseOrderSerializer(purchase, context={"request": request})
            return CreateSuccess(purchase_seria.data)
    except Exception as e:
        transaction.rollback()
        return ServerError(str(e))

#Sale Order API
#----------------------------------------------------------------
@api_view(['POST'])
def create_sale_order(request):
    try:
        with transaction.atomic():
            data = get_data(request, is_form_data=True)
            sale_details = json.loads(data["sale_details"])
            invoices = request.FILES.getlist("invoices")
            warehouse = data["warehouse"]
            #Sales Order
            sale_seria = CreateSaleOrderSerializer(data=data)
            if not sale_seria.is_valid():
                return BadRequest(sale_seria.errors)
            order = sale_seria.save(company_id=data['company_id'])
            #Sale Order Details
            sale_detail_seria = SaleDetailSerializer(data=sale_details, many=True)
            if not sale_detail_seria.is_valid():
                return BadRequest(sale_detail_seria.errors)
            sale_detail_seria.save(order=order)
            #Update Product Variant
            for detail in sale_details:
                variant = ProductVariant.objects.get(company_id=data['company_id'], id=detail['variant'])
                variant.quantity -= detail['quantity']
                variant.save() 
                #Update Inventory
                inventories = Inventory.objects.filter(company_id=data['company_id'], variant=variant, warehouse_id=warehouse).first()
                if inventories.quantity >= detail['quantity']:
                    inventories.quantity -= detail['quantity']
                    inventories.save()
                else:
                    raise ValueError("Số lượng trong kho không đủ để trừ!")
            #Invoices
            for invoice in invoices:
                InvoiceFile.objects.create(company_id=order.company_id, order=order, invoice=invoice)

            sale_seria = SaleOrderSerializer(order, context={"request": request})
            return CreateSuccess(sale_seria.data)
    except Exception as e:
        transaction.rollback()
        return ServerError(str(e))