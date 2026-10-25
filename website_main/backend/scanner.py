from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
import site
import os

for site_pkg in site.getsitepackages() + [site.getusersitepackages()]:
    if site_pkg and os.path.exists(site_pkg):
        dll_path = os.path.join(site_pkg, "pyzbar")
        if os.path.exists(dll_path):
            os.add_dll_directory(dll_path)
            break

def scan_image(userfile):
    image = Image.open(userfile.stream)
    isbns = get_isbn(image)
    return isbns


def get_isbn(image):
    array = decode(image, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray