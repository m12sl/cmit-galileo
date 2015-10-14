__author__ = 'm12sl'
from flask import Flask, jsonify
import redis

app = Flask(__name__)
red = redis.Redis('localhost', port=6379)

@app.route('/')
def hello():
    return "Hello world!"


@app.route('/led')
@app.route('/led/<status>', methods=["POST"])
def led(status=None):
    if status is None:
        return jsonify(led=red.get('led')), 200
    if status == 'on':
        red.set('led', 1)
    elif status == 'off':
        red.set('led', 0)
    else:
        return jsonify(error='wrong status'), 400
    return jsonify(status='ok'), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
