import os

from pyzbar.pyzbar import decode, ZBarSymbol

from PIL import Image
from flask import Flask, render_template, request
scan_app = Flask(__name__) #Defined the app

dll_path = r"C:\Users\tahah\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyzbar\libzbar-64.dll"
os.add_dll_directory(dll_path)


#web page route
@scan_app.route('/')
def home():
    msg = "Test test test"
    return render_template('pages/scanner-page.html', local_message=msg)

@scan_app.route('/scanner-page', methods=['POST'])
def upload_image():
    if ('image') not in request.files:
        return "No image file found in the request", 400

    userfile = request.files['image']
    
    image = Image.open(userfile.stream)
    isbns = get_isbn(image)

    print(isbns[0])



def get_isbn(image):
    img = Image.open(image)
    array = decode(img, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray