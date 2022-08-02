import pyqrcode
import png
from pyqrcode import QRCode

s = "deploy the link which you want to embed in the QR"

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 8)

url.png('myqr9.png', scale = 6)
