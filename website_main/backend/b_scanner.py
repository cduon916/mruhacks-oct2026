from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

import os
dll_path = r"C:\Users\tahah\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyzbar\libzbar-64.dll"
os.add_dll_directory(dll_path)


def scan_image(userfile):
    image = Image.open(userfile.stream)
    isbns = get_isbn(image)

    for isbn in isbns:
        print(isbn + "\n")



def get_isbn(image):
    array = decode(image, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray