# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import request
import requests
app = Flask(__name__)


@app.route("/")
def index():
    return "HEY NIGGA!"


@app.route("/url", methods=['POST'])
def redirect():
    if request.is_json:
        print(request)
        url = request.get_json()['url']
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            return response
        else:
            print(response.json())
    else:
        return json.dumps({'error':'wrong request was sended'})


if __name__ == '__main__':
    app.run(ssl_context='adhoc',host='0.0.0.0',port=443)
