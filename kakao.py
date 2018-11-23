# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════
███████╗██╗   ██╗██╗████████╗███████╗   ██╗      █████╗ ██████╗
██╔════╝██║   ██║██║╚══██╔══╝██╔════╝   ██║     ██╔══██╗██╔══██╗
███████╗██║   ██║██║   ██║   █████╗     ██║     ███████║██████╔╝
╚════██║██║   ██║██║   ██║   ██╔══╝     ██║     ██╔══██║██╔══██╗
███████║╚██████╔╝██║   ██║   ███████╗██╗███████╗██║  ██║██████╔╝
╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝
═══════════════════════════════════════════════════════════════
                Lost Ark wait notifier api
                develop by woosik yoon (yoonwoosik12@naver.com)
                [suitee.me]
═══════════════════════════════════════════════════════════════
"""

from flask import Flask, request, jsonify
from modules.dbtools import *
from modules.crawler import *
from datetime import datetime

app = Flask(__name__)

keyboard_button = {
    "type": "buttons",
    "buttons": ["대기열", "점검 공지", "설명서"]
}

message_button = {
    'message_button': {
        'label': '개발자 윤옴므 블로그',
        'url': 'http://suitee.me'
    }
}

def get_wait_text():
    db = DbTools(select_only=True)
    data = db.get_data()
    now = datetime.now()
    text = "🐤️로스트아크 대기열 알림봇\n"
    text += "═══════════\n"
    text += f"{now.hour}시 {now.minute}분 {now.second}초 기준\n\n"

    for item in data:
        queue = item[1]
        if item[1] == -1:
            queue = '지원예정'

        text += f"{item[0]} : {queue}\n"
    text += f"\n데이터 제공 :\nrubystarashe.github.io/lostark\n"
    db.close()

    return text

def get_notice_text():
    crawler = Crawler(use_driver=False)
    notices = crawler.start_notice()
    text = "🐤️로스트아크 점검 공지\n"
    text += "═══════════\n"
    for notice in notices:
        text += '\n\n'.join(notice)
        text += '\n\n-----------------------\n'

    return text

def get_help_text():
    text = """🐤️알림봇 설명서
═══════════
1. 대기열
현재 대기열을 볼 수 있습니다.

2. 점검 공지
공식 홈페이지의 점검예정인 공지를 볼 수 있습니다.

3. 설명서
로스트아크 대기열 알림봇 설명서 입니다.
    """

    return text

@app.route('/keyboard')
def keyboard():
    data_send = keyboard_button
    return jsonify(data_send)


@app.route('/message', methods=['POST'])
def message():
    data_receive = request.get_json()
    content = data_receive['content']
    if content == u"대기열":
        data_send = {
            "message": {
                "text": get_wait_text()
            }
        }
    elif content == u"점검 공지":
        data_send = {
            "message": {
                "text": get_notice_text()
            }
        }
    elif content == u"설명서":
        data_send = {
            "message": {
                "text": get_help_text()
            }
        }
    else:
        data_send = {
            "message": {
                "text": "명령어를 다시 입력해주세요."
            }
        }

    data_send["message"].update(message_button)
    data_send["keyboard"] = keyboard_button
    return jsonify(data_send)


if __name__ == "__main__":
    app.run(host=config.SERVER_CONFIG['host'], port=config.SERVER_CONFIG['port'])