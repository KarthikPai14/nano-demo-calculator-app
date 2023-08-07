from flask import Flask
import requests

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=requests.get_json()
    if 'first' in data and 'second' in data:
        result=data["first"]+data["second"]
        response=jsonify({"result":result})
    return response,200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if 'first' in data and 'second' in data:
        result=data["first"]-data["second"]
        response=jsonify({"result":result})
    return response,200
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
