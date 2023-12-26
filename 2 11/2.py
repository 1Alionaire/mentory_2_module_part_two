from flask import Flask, Response

app = Flask(__name__)
@app.route('/kek', methods = ['GET'])

def hello():
        try:
            return Response('Hello, World!')
        except:
            return 'Error'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)




