from flask import *
from scanner import scan_image #NEWWW

app = Flask(__name__, template_folder="../templates")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scanner', methods=['GET', 'POST'])
def scanner():

    given_isbn = "No ISBN found"
    if request.method == 'POST':
        image = request.files['image']
        isbn_array = scan_image(image)
        if (len(isbn_array) > 0):
            given_isbn = isbn_array[0]

    return render_template('scanner-page.html', isbn = given_isbn)

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)