from django.urls import path, include

from app.controllers.delivery.create_delivery import create_customer, create_purchase_order, create_sale_order, create_supplier
from app.controllers.delivery.delete_delivery import delete_customer, delete_purchase_order, delete_sale_order, delete_supplier
from app.controllers.delivery.get_delivery import get_customer, get_purchase_order, get_sale_order, get_supplier
from app.controllers.delivery.update_delivery import update_customer, update_purchase_order, update_sale_order, update_supplier


urlpatterns = ([

    #Supplier URL
    path('supplier/create', create_supplier, name="create-supplier"),
    path('supplier/get', get_supplier, name="get-supplier"),
    path('supplier/update/<int:supplier_id>', update_supplier, name="update-supplier"),
    path('supplier/delete/<int:supplier_id>', delete_supplier, name="delete-supplier"),

    #Customer URL
    path('customer/create', create_customer, name="create-customer"),
    path('customer/get', get_customer, name="get-customer"),
    path('customer/update/<int:customer_id>', update_customer, name="update-customer"),
    path('customer/delete/<int:customer_id>', delete_customer, name="delete-custom"),
    
    #PurchaseOrder URL
    path("purchase-order/create", create_purchase_order, name="create-purchase-order"),
    path("purchase-order/get", get_purchase_order, name="get-purchase-order"),
    path("purchase-order/update/<int:purchase_id>", update_purchase_order, name="update-purchase-order"),
    path("purchase-order/delete/<int:purchase_id>", delete_purchase_order, name="delete-purchase-order"),

    #SaleOrder URL
    path("sale-order/create", create_sale_order, name="create-sale-order"),
    path("sale-order/get", get_sale_order, name="get-sale-order"),
    path("sale-order/update/<int:sale_id>", update_sale_order, name="update-sale-order"),
    path("sale-order/delete/<int:sale_id>", delete_sale_order, name="delete-sale-order"),


], 'delivery')
