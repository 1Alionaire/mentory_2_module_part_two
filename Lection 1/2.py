from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/Hello', methods=['GET'])
def hello():
    return jsonify(
        {
            'message':'Hello',
            'pit': ''
        }

    )

if __name__ == '__main__':
    app.run(debug=True)