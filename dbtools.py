# -*- coding: utf-8 -*-
import pymysql.cursors
from crawler import *
import datetime


class DbTools:
    def __init__(self, select_only = False):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password="2913",
                                    charset='utf8')
        self.conn.cursor().execute("USE db;")

        if not select_only:
            self.crawler = Crawler()

    def close(self):
        self.conn.close()
        self.crawler.end()

    def get_data(self):
        cursor = self.conn.cursor()
        cursor.execute("USE db;")

        sql = """
        SELECT      sv.server_name
        ,           que.queue
        FROM        queue AS que
        INNER JOIN  server AS sv
        ON          que.server_id = sv.server_id
        WHERE       que.date_time = (SELECT   date_time
                                     FROM     queue
                                     ORDER BY date_time DESC
                                     LIMIT 1);
        """
        cursor.execute(sql)

        rows = cursor.fetchall()
        return rows

    def insert_queue_query(self, queues):
        cursor = self.conn.cursor()

        for i, queue in enumerate(queues):
            sql_query = f"INSERT INTO queue(date_time, server_id, queue) VALUES (now(), {i + 1}, {queue['queue']});"
            cursor.execute(sql_query)

        self.conn.commit()
        print('{0}개의 정보 업데이트 완료: {1}'.format(len(queues),  str(datetime.datetime.now())))


    def save_data(self):
        json_file = self.crawler.start()

        self.insert_queue_query(json_file['items'])

# try:
#     cursor = conn.cursor()
#
#     cursor.execute("USE db;")
#
#     cr = Crawler()
#     for i in range(5):
#         json_file = cr.start()
#
#         insert_queue_query(json_file['items'], cursor)
#
#         conn.commit()
#         print('정보 업데이트 완료: ' + str(datetime.datetime.now()))
#         sleep(3)
#
# except Exception as e:
#     print("Exeception occured:{}".format(e))
#
# finally:
#     conn.close()
#     cr.end()