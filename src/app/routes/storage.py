from django.urls import path, include

from app.controllers.storage.create_storage import (
    create_product,   
    create_category, 
    create_brand,
    create_warranty,
    create_warehouse,
    upload_excel_and_create_products
)
from app.controllers.storage.delete_storage import (
    delete_brand, 
    delete_category, 
    delete_product, 
    delete_product_variant, 
    delete_warehouse, 
    delete_warranty
)
from app.controllers.storage.get_storage import (
    copy_report_24hrs,
    get_product, 
    get_inventory, 
    get_category, 
    get_brand, 
    get_product_variant,
    get_warranty,
    get_warehouse, 
    get_inventory_report,
    download_excel_template

)
from app.controllers.storage.update_storage import (
    update_brand,
    update_category,
    update_product,
    update_product_variant,
    update_warehouse,
    update_warranty
)

urlpatterns = ([
    #Warehouse URL
    path("warehouse/create", create_warehouse, name="create-warehouse"),
    path("warehouse/get", get_warehouse, name="get-warehouse"),
    path("warehouse/update/<int:warehouse_id>", update_warehouse, name="update-warehouse"),
    path("warehouse/delete/<int:warehouse_id>", delete_warehouse, name="delete-warehouse"),

    #Warranty URL
    path("warranty/create", create_warranty, name="create-warranty"),
    path("warranty/get", get_warranty, name="get-warranty"),
    path("warranty/update/<int:warranty_id>", update_warranty, name="update-warranty"),
    path("warranty/delete/<int:warranty_id>", delete_warranty, name="delete-warranty"),

    #Category URL
    path("category/create", create_category, name="create-category"),
    path("category/get", get_category, name="get-category"),
    path("category/update/<int:category_id>", update_category, name="update-category"),
    path("category/delete/<int:category_id>", delete_category, name="delete-category"),

    #Brand URL
    path("brand/create", create_brand, name="create-brand"),
    path("brand/get", get_brand, name="get-brand"),
    path("brand/update/<int:brand_id>", update_brand, name="update-brand"),
    path("brand/delete/<int:brand_id>", delete_brand, name="delete-brand"),
    
    #Product URL
    path("product/create", create_product, name="create-product"),
    path("product/get", get_product, name="get-product"),
    path("product/update/<int:product_id>", update_product, name="update-product"),
    path("product/delete/<int:product_id>", delete_product, name="delete-product"),
    path("product/variant/get", get_product_variant, name="get-product-variant"),
    path("product/variant/update/<int:variant_id>", update_product_variant, name="update-product-variant"),
    path("product/variant/delete/<int:variant_id>", delete_product_variant, name="delete-product-variant"),
    
    #Inventory URL
    path("inventory/get", get_inventory, name="get-inventory"),
    path("inventory/report/get", get_inventory_report, name="get-inventory"),
    path("inventory/task_24hrs", copy_report_24hrs, name="tasks"),

    #Excel URL
    path("product/download-excel-template", download_excel_template, name="download-excel-template"),
    path("product/upload-excel-product", upload_excel_and_create_products, name="download-excel-template")


], 'storage')
