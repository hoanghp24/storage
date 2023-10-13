#django restframework
from rest_framework.decorators import api_view

#helpers
from app.helpers.response import (
    NotFound, 
    ServerError, 
    UpdateSuccess, 
    BadRequest
)
from app.helpers.common_business import get_data

#models
from app.models.delivery import (
    Customer,
    PurchaseOrder,
    SaleOrder,
    Supplier, 
)

#serializers
from app.serializers.delivery import (
   CreateCustomerSerializer,
   CreateSupplierSerializer,
   CustomerSerializer,
   PurchaseOrderSerializer,
   SaleOrderSerializer,
   SupplierSerializer,
   UpdatePurchaseOrderSerializer,
   UpdateSaleOrderSerializer,
) 

# Create your API here.

# Supplier API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_supplier(request, supplier_id):
    try:
        data = get_data(request)
        supplier = Supplier.objects.filter(id=supplier_id, company_id=data['company_id']).first()
        if supplier is None:
            return NotFound()
        serializer = CreateSupplierSerializer(instance=supplier, data=data)
        if serializer.is_valid():
            supplier = serializer.save()
            result_seria = SupplierSerializer(supplier)
            return UpdateSuccess(result_seria.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()

# Customer API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_customer(request, customer_id):
    try:
        data = get_data(request)
        customer = Customer.objects.filter(id=customer_id, company_id=data['company_id']).first()
        if customer is None:
            return NotFound()
        serializer = CreateCustomerSerializer(instance=customer, data=data)
        if serializer.is_valid():
            customer = serializer.save()
            result_seria = CustomerSerializer(customer)
            return UpdateSuccess(result_seria.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()


# Purchase Order API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_purchase_order(request, purchase_id):
    try:
        data = get_data(request, is_form_data=True)
        purchase = PurchaseOrder.objects.filter(id=purchase_id, company_id=data['company_id']).first()
        if purchase is None:
            return NotFound()
        serializer = UpdatePurchaseOrderSerializer(instance=purchase, data=data)
        if serializer.is_valid():
            purchase = serializer.save()
            result_seria = PurchaseOrderSerializer(purchase)
            return UpdateSuccess(result_seria.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()

# Sale Order API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_sale_order(request, sale_id):
    try:
        data = get_data(request, is_form_data=True)
        sale_order = SaleOrder.objects.filter(id=sale_id, company_id=data['company_id']).first()
        if sale_order is None:
            return NotFound()
        serializer = UpdateSaleOrderSerializer(instance=sale_order, data=data)
        if serializer.is_valid():
            sale_order = serializer.save()
            result_seria = SaleOrderSerializer(sale_order)
            return UpdateSuccess(result_seria.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()