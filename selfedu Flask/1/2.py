# Самый простейший сервер

from flask import Flask
# Присваиваем объекту app

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/about')
def about():
    return "<h1>Обо мне</h1>"

if __name__ == '__main__':
    app.run(debug=True)