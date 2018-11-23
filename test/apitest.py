# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from modules.crawler import *

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    data_send = {
        "type": "buttons",
        "buttons": ["대기열", "도움말"]
    }
    return jsonify(data_send)


@app.route('/message', methods=['POST'])
def Message():
    data_receive = request.get_json()
    print(data_receive)
    content = data_receive['content']
    if content == u"대기열":
        data_send = {
            "message": {
                "text": ""
            }
        }

    data_send["message"].update({'message_button': {'label': '개발자 윤옴므 블로그', 'url': 'http://suitee.me'}})
    data_send["keyboard"] = {"type": "buttons", "buttons": ["대기열", "도움말"]}
    return jsonify(data_send)

if __name__ == "__main__":
    app.run(host=config.SERVER_CONFIG['host'], port=config.SERVER_CONFIG['port'])