# -*- coding: utf-8 -*-
from dbtools import DbTools
import datetime

db = DbTools(select_only=True)

for i in range(10):
    data = db.get_data()
    now = datetime.datetime.now()
    text = "🐤️로스트아크 대기열 알림봇\n"
    text += "═══════════\n"
    text += f"{now.hour}시 {now.minute}분 {now.second}초 기준\n\n"

    for item in data:
        queue = item[1]
        if item[1] == -1:
            queue = '지원예정'

        text += f"{item[0]} : {queue}\n"

    print(text)

