from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


# Add username after the /name
@app.route('/name/<username>')
def name(username):
    return f'Welcome {username} to my absolutely useless website'


# Just for integer
@app.route('/name/<int:num>')
def number(num):
    return f'Welcome {num} to my absolutely useless website'


# Should be in a directory called templates
@app.route('/html/<username>')
def render_page(username):
    return render_template('home.html', usernameHtml=username)


if __name__ == '__main__':
    app.run(debug=True)
