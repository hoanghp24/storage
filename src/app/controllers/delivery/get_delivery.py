#django restframework
from rest_framework.decorators import api_view

#models
from app.models.delivery import Customer, PurchaseOrder, SaleOrder, Supplier

#querydb
from app.querydb import (
    query_get_customer, 
    query_get_purchase_order, 
    query_get_sale_order, 
    query_get_supplier
)

#serializers
from app.serializers.delivery import (
    CustomerSerializer, 
    PurchaseOrderSerializer, 
    SaleOrderSerializer, 
    SupplierSerializer
)

#helpers
from app.helpers.common_business import  get_querystring
from app.helpers.response import GetSuccess, NotFound, ServerError, result_page_info



# Create your API here.

#Supplier API
#----------------------------------------------------------------
@api_view(['GET'])
def get_supplier(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'supplier_id'])
        query = query_get_supplier(company_id, query_string)
        result_query = Supplier.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['supplier_id'] and total == 0:
            return NotFound()
        if not query_string['supplier_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = SupplierSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Customer API
#----------------------------------------------------------------
@api_view(['GET'])
def get_customer(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'customer_id'])
        query = query_get_customer(company_id, query_string)
        result_query = Customer.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['customer_id'] and total == 0:
            return NotFound()
        if not query_string['customer_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = CustomerSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Purchase Order API
#----------------------------------------------------------------
@api_view(['GET'])
def get_purchase_order(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'purchase_id', 'sortDate', 
                                                             'warehouse_id', 'start_date', 'end_date'])
        query = query_get_purchase_order(company_id, query_string)
        result_query = PurchaseOrder.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['purchase_id'] and total == 0:
            return NotFound()
        if not query_string['purchase_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = PurchaseOrderSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Sale Order API
#----------------------------------------------------------------
@api_view(['GET'])
def get_sale_order(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'sale_id', 'sortDate', 
                                                             'warehouse_id', 'start_date', 'end_date'])
        query = query_get_sale_order(company_id, query_string)
        result_query = SaleOrder.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['sale_id'] and total == 0:
            return NotFound()
        if not query_string['sale_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = SaleOrderSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()