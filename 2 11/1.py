from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/kek', methods = ['GET'])
def hello():
    return jsonify(
        {
            'message' : 'Hello from my notebook'
        }
    )

if __name__ == '__main__':
    app.run(debug=True)

