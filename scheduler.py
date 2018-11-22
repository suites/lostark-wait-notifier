# -*- coding: utf-8 -*-
import schedule
import time
from datetime import datetime
from dbtools import DbTools

db = DbTools(select_only=False)

def schedule_job():
    db.save_data()

if __name__ == "__main__":
    print("scheduler is running! {}".format(datetime.now()))

    schedule.every(2).seconds.do(schedule_job)
    while True:
        schedule.run_pending()
        time.sleep(1)