import pyqrcode
import png
from pyqrcode import QRCode

s = "https://drive.google.com/file/d/1_L_ULC-TBNFSM5kXRrfmKEzum2KlaUEK/view?usp=sharing"

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 8)

url.png('myqr9.png', scale = 6)
