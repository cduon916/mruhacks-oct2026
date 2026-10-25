from flask import *
from scanner import scan_image #NEWWW
from game import get_char

isbn = 0

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
    if (given_isbn != "No ISBN found"):
        return render_template('scanner-page.html', isbn = given_isbn)
    else:
        return render_template('game.html', isbn_num = given_isbn)

@app.route('/game', methods=['GET', 'POST','SHOW'])
def game():
    if request.method == 'SHOW':
        character = get_char(isbn)
    return render_template('game.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)