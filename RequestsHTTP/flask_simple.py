from flask import Flask

from api_request import Requesta

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


@app.route('/bahaa')
def bahaa():
    return "U are in Bahaa route"


@app.route('/get_houses')
def get_all_houses():
    return Requesta.get_all_houses('stam')


if __name__ == '__main__':
    app.run(debug=True)
