# django restframework
import json
from rest_framework import serializers

# django
from django.conf import settings

# helpers
from app.helpers.generate_code_img import generate_random_digits

# models
from app.models.storage import (
    Category,
    Brand,
    Property,
    Warehouse,
    Product,
    Warranty,
    ProductVariant,
    Inventory,
    InventoryReport,
)

# Create your serializers here.


# Warehouse Serializer
# ----------------------------------------------------------------
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {
            "sku": {"read_only": True},
        }

    def create(self, validated_data):
        warehouse = Warehouse.objects.create(**validated_data)
        warehouse.sku = f"WH{str(warehouse.id).zfill(5)}"
        warehouse.save()
        return warehouse


# Warranty Serializer
# ----------------------------------------------------------------
class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = "__all__"


# Category Serializer
# ----------------------------------------------------------------
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField("get_children")

    class Meta:
        model = Category
        fields = "__all__"

    def get_children(self, obj):
        serializer = CategorySerializer(obj.children, many=True)
        return serializer.data


# Brand Serializer
# ----------------------------------------------------------------
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


# Product Serializer
# ----------------------------------------------------------------
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "sku", "qrcode", "unit"]

    def create(self, validated_data):
        sku = validated_data.pop("sku")
        product = Product.objects.create(**validated_data)
        product.sku = f"PVN{str(product.id).zfill(5)}" if not sku else sku
        product.save()
        return product


class CreateProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["name", "image", "price", "cost", "unit", "quantity"]

    def create(self, validated_data):
        variant = ProductVariant.objects.create(**validated_data)
        variant.sku = f"{variant.product.sku}{variant.id}"
        variant.barcode = generate_random_digits()
        variant.save()

        warehouses = Warehouse.objects.all()
        for warehouse in warehouses:
            Inventory.objects.create(
                company_id=variant.company_id,
                variant=variant,
                warehouse=warehouse,
                quantity=variant.quantity,
            )
        return variant


class ProductVariantSerializer(serializers.ModelSerializer):
    barcode_image = serializers.SerializerMethodField("get_barcode")
    image = serializers.SerializerMethodField("get_image")

    class Meta:
        model = ProductVariant
        fields = "__all__"
        extra_kwargs = {"sku": {"read_only": True}, "product": {"read_only": True}}

    def to_representation(self, instance):
        self.fields["warehouse"] = WarehouseSerializer(read_only=True)
        return super(ProductVariantSerializer, self).to_representation(instance)

    def get_barcode(self, obj):
        if obj.barcode_image:
            return settings.HOST_URL + obj.barcode_image.url
        return None

    def get_image(self, obj):
        if obj.barcode_image:
            path = "/media/product/company_{}/".format(obj.company_id)
            return settings.HOST_URL + path + obj.image
        return None


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    qrcode = serializers.SerializerMethodField("get_qrcode")
    images = serializers.SerializerMethodField("get_list_images")
    image = serializers.SerializerMethodField("get_image_product")
    variants = ProductVariantSerializer(many=True)
    properties = PropertiesSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["category"] = CreateCategorySerializer(read_only=True)
        self.fields["brand"] = BrandSerializer(read_only=True)
        self.fields["warranty"] = WarrantySerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)

    def get_list_images(self, obj):
        return [f"{settings.HOST_URL}{image.image.url}" for image in obj.images.all()]

    def get_image_product(self, obj):
        if obj.image:
            return settings.HOST_URL + obj.image.url
        return None

    def get_qrcode(self, obj):
        if obj.qrcode:
            return settings.HOST_URL + obj.qrcode.url
        return None


# Invetory Serializer
# ----------------------------------------------------------------
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["variant"] = ProductVariantSerializer(read_only=True)
        self.fields["warehouse"] = WarehouseSerializer(read_only=True)
        return super(InventorySerializer, self).to_representation(instance)


class InventoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryReport
        fields = "__all__"
        extra_kwargs = {
            "inventory": {"write_only": True},
        }
