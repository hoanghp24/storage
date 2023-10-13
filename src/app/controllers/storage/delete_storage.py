#django restframework
from rest_framework.decorators import api_view

#helpers
from app.helpers.response import (
    BadRequest,
    NotFound, 
    ServerError, 
    DeleteSuccess
)
from app.helpers.common_business import get_data

#models
from app.models.storage import (
    Product,
    ProductVariant,
    Category,
    Warehouse,
    Warranty,
    Brand
)


# Create your API here.

# Warehouse API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_warehouse(request, warehouse_id):
    try:
        data = get_data(request)
        warehouse = Warehouse.objects.filter(id=warehouse_id, company_id=data['company_id']).first()
        if warehouse is None:
            return NotFound()
        warehouse.delete()
        return DeleteSuccess()
    except:
        return ServerError()

# Warranty API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_warranty(request, warranty_id):
    try:
        data = get_data(request)
        warranty = Warranty.objects.filter(id=warranty_id, company_id=data['company_id']).first()
        if warranty is None:
            return NotFound()
        warranty.delete()
        return DeleteSuccess()
    except:
        return ServerError()


# Category API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_category(request, category_id):
    try:
        data = get_data(request)
        category = Category.objects.filter(id=category_id, company_id=data['company_id']).first()
        if category is None:
            return NotFound()
        category.delete()
        return DeleteSuccess()
    except:
        return ServerError()

# Brand API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_brand(request, brand_id):
    try:
        data = get_data(request)
        brand = Brand.objects.filter(id=brand_id, company_id=data['company_id']).first()
        if brand is None:
            return NotFound()
        brand.delete()
        return DeleteSuccess()
    except:
        return ServerError()
    
# Product API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        data = get_data(request)
        product = Product.objects.filter(id=product_id, company_id=data['company_id']).first()
        if product is None:
            return NotFound()
        variant = ProductVariant.objects.filter(product_id=product_id)
        if variant is None:
            product.delete()
            return DeleteSuccess()
        return BadRequest("Product variants greater than 0, the product cannot be deleted!")
    except:
        return ServerError()

# ProductVariant API
# ----------------------------------------------------------------
@api_view(['DELETE'])
def delete_product_variant(request, variant_id):
    try:
        data = get_data(request)
        variant = ProductVariant.objects.filter(id=variant_id, company_id=data['company_id']).first()
        if variant is None:
            return NotFound()
        variant.delete()
        return DeleteSuccess()
    except:
        return ServerError()