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

    given_isbn = ""
    if request.method == 'POST':
        image = request.files['image']
        isbn_array = scan_image(image)
        if (len(isbn_array) > 0):
            given_isbn = isbn_array[0]

    if (str(given_isbn).isdigit()):
        return redirect(url_for("game", isbn=given_isbn))
    
    if (request.method == 'GET'):
        return render_template('scanner-page.html', isbn = given_isbn)
    
    #return render_template('scanner-page.html', isbn = "Invalid ISBN! Try again.")

@app.route('/game', methods=['GET', 'POST'])
def game():
    isbn = request.args.get('isbn', '')

    if (isbn.isdigit()):
        character = get_char(int(isbn))
        app.logger.info(character.name)

    if request.method == 'GET':
        return render_template('game.html', isbn=isbn)
    
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)