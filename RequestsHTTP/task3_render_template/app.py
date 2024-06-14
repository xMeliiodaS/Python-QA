from flask import Flask, render_template


class App:
    app = Flask(__name__)

    @staticmethod
    @app.route('/')
    def first_page():
        return "Hey, welcome to the home page"

    @staticmethod
    @app.route('/home')
    @app.route('/home/<user>')
    def home(user=""):
        return render_template('home.html', username=user)

    @staticmethod
    @app.route('/profile/<user>')
    def profile(user=""):
        user_data = {
            'username': user,
            'name': user.capitalize(),
            'email': f'{user}@example.com',
            'joined_date': '2024-01-01'
        }
        return render_template('profile.html', user=user_data)
