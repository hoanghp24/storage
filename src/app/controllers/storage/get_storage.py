#django restframework
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from openpyxl import Workbook
from django.http import HttpResponse
#helpers
from app.helpers.common_business import get_querystring
from app.helpers.response import GetSuccess, NotFound, ServerError, result_page_info

#models
from app.models.storage import (
    Brand, 
    Category, 
    InventoryReport, 
    Product, 
    ProductVariant, 
    Warehouse, 
    Warranty, 
    Inventory
)

#querydb
from app.querydb import (
    query_get_brand, 
    query_get_category, 
    query_get_inventory, 
    query_get_inventory_report, 
    query_get_product, 
    query_get_product_variant, 
    query_get_warehouse, 
    query_get_warranty
)
#serializers
from app.serializers.storage import (
    InventoryReportSerializer,
    ProductSerializer, 
    BrandSerializer, 
    CategorySerializer, 
    InventorySerializer, 
    ProductVariantSerializer,
    WarrantySerializer,
    WarehouseSerializer
)

# Create your API here.

#Warehouse API
#----------------------------------------------------------------
@api_view(['GET'])
def get_warehouse(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'warehouse_id', 'start_date', 'end_date'])
        query = query_get_warehouse(company_id, query_string)
        result_query = Warehouse.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['warehouse_id'] and total == 0:
            return NotFound()
        elif not query_string['warehouse_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = WarehouseSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Warranty API
#----------------------------------------------------------------
@api_view(['GET'])
def get_warranty(request):
    try:
        company_id, query_string = get_querystring(request, ['warranty_id'])
        query = query_get_warranty(company_id, query_string)
        result_query = Warranty.objects.raw(query)
        if not result_query:
            return NotFound()
        serializer = WarrantySerializer(result_query, many=True)
        return GetSuccess(serializer.data)
    except:
        return ServerError()

#Category API
#----------------------------------------------------------------
@api_view(['GET'])
def get_category(request):
    try:
        company_id, query_string = get_querystring(request, ['parent_id', 'search_text'])
        query = query_get_category(company_id, query_string)
        result_query = Category.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['parent_id'] and total == 0:
            return NotFound()
        elif not query_string['parent_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = CategorySerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Brand API
#----------------------------------------------------------------
@api_view(['GET'])
def get_brand(request):
    try:
        company_id, query_string = get_querystring(request, ['brand_id', 'search_text'])
        query = query_get_brand(company_id, query_string)
        result_query = Brand.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['brand_id'] and total == 0:
            return NotFound()
        elif not query_string['brand_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = BrandSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()

#Product API
#----------------------------------------------------------------
@api_view(['GET'])
def get_product(request):
    try:
        company_id, query_string = get_querystring(request, ['search_text', 'product_id', 'start_date', 'end_date', 'sortDate'])
        query = query_get_product(company_id, query_string)
        result_query = Product.objects.raw(query)
        total = result_query[0].total if result_query else 0
        page_info = {}
        if query_string['product_id'] and total == 0:
            return NotFound()
        elif not query_string['product_id']:
            page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        serializer = ProductSerializer(result_query, many=True)
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
#Product Variant API
#----------------------------------------------------------------
@api_view(['GET'])
def get_product_variant(request):
    try:
        company_id, query_string = get_querystring(request, ['product_id'])
        query = query_get_product_variant(company_id, query_string)
        result_query = ProductVariant.objects.raw(query)
        total = result_query[0].total if result_query else 0
        if query_string['product_id'] and total == 0:
            return NotFound()
        serializer = ProductVariantSerializer(result_query, many=True)
        page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()

#Inventory API
#----------------------------------------------------------------
@api_view(['GET'])
def get_inventory(request):
    try:
        company_id, query_string = get_querystring(request, ['variant_id', 'warehouse_id', 'start_date', 'end_date'])
        query = query_get_inventory(company_id, query_string)
        result_query = Inventory.objects.raw(query)
        total = result_query[0].total if result_query else 0
        if query_string['variant_id'] and total == 0:
            return NotFound()
        serializer = InventorySerializer(result_query, many=True, context= {"request":request})
        page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
@api_view(['GET'])
def get_inventory_report(request):
    try:
        company_id, query_string = get_querystring(request, ['start_date', 'end_date'])
        query = query_get_inventory_report(company_id, query_string)
        result_query = InventoryReport.objects.raw(query)
        total = result_query[0].total if result_query else 0
        serializer = InventoryReportSerializer(result_query, many=True, context= {"request":request})
        page_info = result_page_info(total, query_string['limit'], query_string['offset'], query_string['page'])
        return GetSuccess(serializer.data, page_info=page_info)
    except:
        return ServerError()
    
@api_view(['GET'])
def copy_report_24hrs(request):
    try:
        inventories = Inventory.objects.all()
        # Sao chép dữ liệu từ Inventory sang InventoryReport cho mỗi Inventory
        for inventory in inventories:
            inventory_serializer = InventorySerializer(inventory)
            inventory_report = InventoryReport.objects.create(
                company_id=inventory.company_id,
                inventory=inventory,
                inventory_data=inventory_serializer.data
            )
            inventory_report.save()
        
        return GetSuccess("Data is copied successfully!")
    except Exception as e:
        return str(e)
    

@api_view(["GET"])
@permission_classes([AllowAny])
def download_excel_template(request):
    try:
        # Tạo một workbook và một worksheet
        wb = Workbook()
        ws = wb.active

        # Thêm dữ liệu mẫu vào worksheet
        # Thay thế các dòng dưới đây bằng cấu trúc dữ liệu thực tế
        headers = ["company_id", "sku", "name", "barcode", "category", "brand", "warranty", "description", "properties", "variants"]
        sample_data = [
            [1, "SKU-001", "Product 1", "12345", "Category A", "Brand X", "1 Year", "Product description", '[]', '[]'],
            [2, "SKU-002", "Product 2", "67890", "Category B", "Brand Y", "2 Years", "Product description", '[]', '[]']
        ]

        ws.append(headers)
        for row in sample_data:
            ws.append(row)

        # Tạo HTTPResponse để trả về tệp Excel
        # Tạo một HTTP response để trả về tệp Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=product_data_template.xlsx'
        # Lưu Workbook vào response
        wb.save(response)

        return response

    except Exception as e:
        return ServerError(str(e))
    
