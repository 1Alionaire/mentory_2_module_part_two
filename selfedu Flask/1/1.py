# Самый простейший сервер

from flask import Flask
# Присваиваем объекту app
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)