from io import BytesIO
from django.core.files import File
import random
import string

#python-qrcode
import qrcode
from PIL import Image

#python-barcode
import barcode
from barcode.writer import ImageWriter
from barcode import Code128 

#Random 13 numbers
#----------------------------------------------------------------
def generate_random_digits():
    return ''.join([str(random.randint(0, 9)) for _ in range(13)])

#Generate QR Code
#----------------------------------------------------------------
def generate_qrcode_img(item):
    qrcode_img=qrcode.make(f'{item.id}')
    canvas =Image.new("RGB", (300,300),"white")
    canvas.paste(qrcode_img)
    fname = str(item.id) + '.png'
    stream = BytesIO()
    canvas.save(stream, 'PNG')
    item.qrcode.save(fname, File(stream))
    canvas.close()
    return item

#Generate Barcode
#----------------------------------------------------------------
def generate_bar_code_img(item):
    barcode_data = str(item.barcode)
    barcode_class = Code128 
    code128 = barcode_class(barcode_data, writer=ImageWriter())
    buffer = BytesIO()
    code128.write(buffer)
    file_name = barcode_data + '.png'
    item.barcode_image.save(file_name, File(buffer), save=False)
    return item