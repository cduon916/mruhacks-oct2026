from flask import *
from scanner import scan_image #NEWWW
from game import get_char, random_char, Character
from bookdatabase import isbn_database
import random

isbn = 0

app = Flask(
    __name__, 
    template_folder="../templates",
    static_folder="../static"
    )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scanner', methods=['GET', 'POST'])
def scanner():

    given_isbn = ""
    if request.method == 'POST':
        image = request.files['image']
        isbn_array = scan_image(image)
        if (isbn_array and len(isbn_array) > 0):
            given_isbn = isbn_array[0]

    if (str(given_isbn).isdigit()):
        return redirect(url_for("game", isbn=given_isbn))
    
    if (request.method == 'GET'):
        return render_template('scanner-page.html', isbn = given_isbn)
    
    return render_template('scanner-page.html', isbn = "Invalid ISBN! Try again.")

@app.route('/game', methods=['GET', 'POST'])
def game():
    isbn = request.args.get('isbn', '')
    enemy = random_char()

    if (isbn.isdigit()):
        character = get_char(int(isbn))
    else:
        character = "Invalid"

    if (character == "Invalid"):
        app.logger.error("Invalid ISBN")
        return redirect(url_for("scanner", isbn=isbn))

    if request.method == 'GET':
        return render_template('game.html', isbn=isbn, player=character.char_to_dict(), enemy=enemy.char_to_dict())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)