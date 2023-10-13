from __future__ import absolute_import, unicode_literals
import logging
from app.serializers.storage import InventorySerializer

from config.celery import app
from app.models.storage import Inventory, InventoryReport

logger = logging.getLogger("celery")


@app.task
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
        
        # Ghi log khi tác vụ hoàn thành thành công
        logger.info("-" * 25)
        logger.info("Data is copied successfully!")
        logger.info("-" * 25)

        return "Data is copied successfully!"
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return str(e)
    