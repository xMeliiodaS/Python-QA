from flask import Flask


class FlaskApp:
    app = Flask(__name__)

    @staticmethod
    @app.route('/')
    def home():
        return "Hey, welcome to the home page"

    @staticmethod
    @app.route('/about')
    def about():
        return "This app is very good my friend, please believe me."
