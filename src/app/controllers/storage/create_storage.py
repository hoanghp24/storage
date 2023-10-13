# django restframework
from app.helpers.generate_code_img import generate_bar_code_img, generate_qrcode_img
from rest_framework.decorators import api_view
from django.db import transaction
import json
from tablib import Dataset

# helpers
from app.helpers.response import BadRequest, CreateSuccess, ServerError
from app.helpers.common_business import get_data
from app.models.storage import Product, ProductImage, Property

# serializers
from app.serializers.storage import (
    BrandSerializer,
    CreateCategorySerializer,
    CreateProductSerializer,
    CreateProductVariantSerializer,
    ProductSerializer,
    PropertiesSerializer,
    WarehouseSerializer,
    WarrantySerializer,
)

# Create your API here.


# Warehouse API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_warehouse(request):
    try:
        data = get_data(request)
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company_id=data["company_id"])
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()


# Warranty API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_warranty(request):
    try:
        data = get_data(request)
        serializer = WarrantySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company_id=data["company_id"])
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()


# Category API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_category(request):
    try:
        data = get_data(request)
        serializer = CreateCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company_id=data["company_id"])
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()


# Brand API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_brand(request):
    try:
        data = get_data(request)
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company_id=data["company_id"])
            return CreateSuccess(serializer.data)
        return BadRequest(serializer.errors)
    except:
        return ServerError()


# Product API
# ----------------------------------------------------------------
@api_view(["POST"])
def create_product(request):
    try:
        with transaction.atomic():
            data = get_data(request, is_form_data=True)
            variants = data["variants"]
            barcode = data.get("barcode")
            images = request.FILES.getlist("images")
            properties = data["properties"]

            # Product
            product_serial = CreateProductSerializer(data=data)
            if not product_serial.is_valid():
                return BadRequest(product_serial.errors)
            product = product_serial.save(company_id=data["company_id"])
            product.image = images[0] if images else None  # Lấy image đầu tiên
            generate_qrcode_img(product)

            # Variants
            variants_serial = CreateProductVariantSerializer(
                data=json.loads(variants), many=True
            )
            if not variants_serial.is_valid():
                return BadRequest(variants_serial.errors)
            variants = variants_serial.save(
                company_id=data["company_id"], product=product
            )
            for variant in variants:
                variant.barcode = variant.sku if not barcode else barcode
                generate_bar_code_img(variant)
                variant.save()

            # ProductImage
            for image in images:
                ProductImage.objects.create(
                    company_id=product.company_id, product=product, image=image
                )

            # Property
            position = 1
            for item in json.loads(properties):
                property = Property(
                    company_id=product.company_id,
                    product=product,
                    name=item["name"],
                    value=item["value"],
                    position=position,
                )
                property.save()
                position += 1

            result = ProductSerializer(product, context={"request": request})
            return CreateSuccess(result.data)
    except Exception as e:
        transaction.rollback()
        return ServerError(str(e))


@api_view(['POST'])
def upload_file_product(request):
    try:
        dataset = Dataset()
        file = request.FILES['file']
        imported_data = dataset.load(file.read(),format='xlsx')
        for data in imported_data:

            product_seria = CreateProductSerializer(data=data)
            if product_seria.is_valid():
                asset_data = product_seria.validated_data
            name = row[0]
            sku = row[1]
            barcode = row[2]
            unit = row[3]

            with transaction.atomic():  
                
        return CreateSuccess("Done")

    except Exception as e:
        return ServerError(str(e))