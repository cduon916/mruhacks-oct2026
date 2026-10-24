from flask import *
from scanner import scan_image #NEWWW

app = Flask(__name__, template_folder="../templates")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        image = request.files['image']
        scan_image(image)

    return render_template('scanner-page.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)