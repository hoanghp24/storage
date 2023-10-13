#django restframework
from rest_framework.decorators import api_view

#helpers
from app.helpers.response import (
    NotFound, 
    ServerError, 
    DeleteSuccess
)
from app.helpers.common_business import get_data

#models
from app.models.delivery import (
    Customer,
    PurchaseOrder,
    SaleOrder,
    Supplier, 
)


# Create your API here.

# Supplier API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_supplier(request, supplier_id):
    try:
        data = get_data(request)
        supplier = Supplier.objects.filter(id=supplier_id, company_id=data['company_id']).first()
        if supplier is None:
            return NotFound()
        supplier.delete()
        return DeleteSuccess()
    except:
        return ServerError()

# Customer API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_customer(request, customer_id):
    try:
        data = get_data(request)
        customer = Customer.objects.filter(id=customer_id, company_id=data['company_id']).first()
        if customer is None:
            return NotFound()
        customer.delete()
        return DeleteSuccess()
    except:
        return ServerError()


# Purchase Order API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_purchase_order(request, purchase_id):
    try:
        data = get_data(request)
        purchase = PurchaseOrder.objects.filter(id=purchase_id, company_id=data['company_id']).first()
        if purchase is None:
            return NotFound()
        purchase.delete()
        return DeleteSuccess()
    except:
        return ServerError()

# Sale Order API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_sale_order(request, sale_id):
    try:
        data = get_data(request)
        sale_order = SaleOrder.objects.filter(id=sale_id, company_id=data['company_id']).first()
        if sale_order is None:
            return NotFound()
        sale_order.delete()
        return DeleteSuccess()
    except:
        return ServerError()