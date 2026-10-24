from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image

img = Image.open("image.png")
array = decode(img)

for code in array:
    number = code.data.decode("utf-8")
    print(number)