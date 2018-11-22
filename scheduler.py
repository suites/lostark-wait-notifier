# -*- coding: utf-8 -*-
import schedule
import time
from datetime import datetime
from dbtools import DbTools

db = DbTools(select_only=False)

def insert_schedule():
    db.save_data()

def delete_schedule():
    db.delete_data()

if __name__ == "__main__":
    print("scheduler is running! {}".format(datetime.now()))

    schedule.every(2).seconds.do(insert_schedule)
    schedule.every(4000).seconds.do(delete_schedule)
    while True:
        schedule.run_pending()
        time.sleep(1)