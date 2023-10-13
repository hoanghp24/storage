import os


# Create your custom here.

# location img qr_code
def location_qrcode_img(instance, filename):
  company_id = instance.company_id
  return os.path.join("qrcode/company_{}/".format(company_id), filename)


# location img barcode
def location_barcode_img(instance, filename):
  company_id = instance.company_id
  return os.path.join("barcode/company_{}/".format(company_id), filename)


# location image item
def location_img(instance, filename):
  company_id = instance.company_id
  return os.path.join("product/company_{}/".format(company_id), filename)

# location file item
def location_file(instance, filename):
  company_id = instance.company_id
  return os.path.join("invoice/company_{}/".format(company_id), filename)