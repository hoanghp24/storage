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
from app.models.storage import (
    Brand, 
    Category,
    Product,
    ProductVariant, 
    Warehouse, 
    Warranty
)

#serializers
from app.serializers.storage import (
    BrandSerializer, 
    CreateCategorySerializer,
    ProductSerializer,
    ProductVariantSerializer, 
    WarehouseSerializer, 
    WarrantySerializer
)

# Create your API here.

# Warehouse API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_warehouse(request, warehouse_id):
    try:
        data = get_data(request)
        warehouse = Warehouse.objects.filter(id=warehouse_id, company_id=data['company_id']).first()
        if warehouse is None:
            return NotFound()
        serializer = WarehouseSerializer(instance=warehouse, data=data)
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()

# Warranty API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_warranty(request, warranty_id):
    try:
        data = get_data(request)
        warranty = Warranty.objects.filter(id=warranty_id, company_id=data['company_id']).first()
        if warranty is None:
            return NotFound()
        serializer = WarrantySerializer(instance=warranty, data=data)
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()

# Category API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_category(request, category_id):
    try:
        data = get_data(request)
        category = Category.objects.filter(id=category_id, company_id=data['company_id']).first()
        if category is None:
            return NotFound()
        serializer = CreateCategorySerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()
    
# Brand API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_brand(request, brand_id):
    try:
        data = get_data(request)
        brand = Brand.objects.filter(id=brand_id, company_id=data['company_id']).first()
        if brand is None:
            return NotFound()
        serializer = BrandSerializer(instance=brand, data=data)
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()
    
# Product API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_product(request, product_id):
    try:
        data = get_data(request, is_form_data=True)
        product = Product.objects.filter(id=product_id, company_id=data['company_id']).first()
        if product is None:
            return NotFound()
        serializer = ProductSerializer(instance=product, data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()
    
# Product Variant API
# ----------------------------------------------------------------
@api_view(['PATCH'])
def update_product_variant(request, variant_id):
    try:
        data = get_data(request)
        variant = ProductVariant.objects.filter(id=variant_id, company_id=data['company_id']).first()
        if variant is None:
            return NotFound()
        serializer = ProductVariantSerializer(instance=variant, data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return UpdateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()
        