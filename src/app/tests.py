from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from app.models.storage import Inventory, InventoryReport, Product, ProductImage, ProductVariant, Property
from app.tasks import copy_report_24hrs

# Create your tests here.


class TestCreateReport(TestCase):
    def test_copy_report_24hrs(self):
        inventory = Inventory.objects.create(company_id=1, variant_id=1)
        result = copy_report_24hrs(None)
        inventory_report = InventoryReport.objects.first()
        self.assertEqual(result, "Data is copied successfully!")
        self.assertIsNotNone(inventory_report)
        self.assertEqual(inventory_report.company_id, inventory.company_id)
        self.assertEqual(inventory_report.inventory, inventory)
        inventory.delete()
        inventory_report.delete()
    