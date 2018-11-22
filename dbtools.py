# -*- coding: utf-8 -*-
import pymysql.cursors
from crawler import *
from datetime import datetime


class DbTools:
    def __init__(self, select_only = False):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password="2913",
                                    charset='utf8')
        self.conn.cursor().execute("USE db;")
        self.crawler = None

        if not select_only:
            self.crawler = Crawler()

    def close(self):
        self.conn.close()
        if self.crawler is not None:
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

    def delete_data(self):
        cursor = self.conn.cursor()
        cursor.execute("USE db;")

        sql = """
        DELETE FROM queue
        ORDER BY date_time ASC LIMIT 9000;
        """
        cursor.execute(sql)

        self.conn.commit()
        print('9000개의 정보 삭제 완료: {0}'.format(str(datetime.now())))

    def insert_queue_query(self, queues):
        cursor = self.conn.cursor()

        for i, queue in enumerate(queues):
            sql_query = f"INSERT INTO queue(date_time, server_id, queue) VALUES (now(), {i + 1}, {queue['queue']});"
            cursor.execute(sql_query)

        self.conn.commit()
        print('{0}개의 정보 업데이트 완료: {1}'.format(len(queues),  str(datetime.now())))


    def save_data(self):
        json_file = self.crawler.start()

        self.insert_queue_query(json_file['items'])