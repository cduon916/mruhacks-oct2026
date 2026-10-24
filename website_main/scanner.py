from pyzbar.pyzbar import decode, ZBarSymbol

from PIL import Image
from flask import Flask, render_template
scan_app = Flask(__name__) #Defined the app

#web page route
@scan_app.route('/')
def home():
    msg = "Test test test"
    return render_template('pages/scanner-page.html', local_message=msg)

#def upload_image():
    

def get_isbn(image):
    img = Image.open(image)
    array = decode(img, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray