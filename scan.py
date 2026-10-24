from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

def get_isbn(image):
    img = Image.open(image)
    array = decode(img, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray

img = Image.open("bookimg.png")
array = get_isbn("bookimg.png")
for n in array:
    print(n + "\n")