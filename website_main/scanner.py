import os

from pyzbar.pyzbar import decode, ZBarSymbol

from PIL import Image
from flask import *
scan_app = Flask(__name__) #Defined the apppy 

dll_path = r"C:\Users\tahah\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyzbar\libzbar-64.dll"
os.add_dll_directory(dll_path)


#web page route
@scan_app.route('/')
def home():
    msg = "Test test test home page"
    return render_template('pages/scanner-page.html', local_message=msg)

@scan_app.route('/', methods=['POST'])
def scan_image():
    userfile = request.files['placeholder']
    
    image = Image.open(userfile.stream)
    isbns = get_isbn(image)

    for isbn in isbns:
        app.logger.info(f"{isbn}")



def get_isbn(image):
    img = Image.open(image)
    array = decode(img, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray