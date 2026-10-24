from flask import Flask, request, render_template
from scanner import scan_image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        image = request.files['image']
        scan_image(image)

    return render_template('scanner.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)