# -*- coding: utf-8 -*-
import pymysql.cursors
from crawler import *


conn = pymysql.connect(host='localhost',
                       user='user',
                       password="2913",
                       charset='utf8mb4')

def create_tables_query():
    sql_query = """
    CREATE DATABASE db;
    USE db;
    
    CREATE TABLE server (
      server_id INT(100) unsigned NOT NULL AUTO_INCREMENT,
      server_name VARCHAR(100) NOT NULL,
      PRIMARY KEY (server_id)
    );
    CREATE INDEX IDX_SERVER_ID ON server(server_id);
    
    CREATE TABLE queue (
      date_time DATETIME NOT NULL,
      server_id INT(100) NOT NULL,
      queue INT(100) NOT NULL,
      PRIMARY KEY (date_time, server_id)
    );
    CREATE INDEX IDX_SERVER_ID ON queue(server_id);
    CREATE INDEX IDX_DATE_TIME ON queue(date_time desc);
    """

    return sql_query


def insert_server_query(servers, cursorObject):
    sql_query = ''
    for server in servers:
        sql_query = f'INSERT INTO server(server_name) VALUES ("{server["server"]}");'
        cursorObject.execute(sql_query)


def insert_queue_query(queues, cursorObject):
    sql_query = ''
    for i, queue in enumerate(queues):
        sql_query += f"INSERT INTO queue(date_time, server_id, queue) VALUES (now(), {i}, {queue['queue']});"
        cursorObject.execute(sql_query)
    # return sql_query


try:
    cursorObject = conn.cursor()

    # WARN:USE IF YOU WANT TO CREATE A TABLE!
    # cursorObject.execute(create_tables_query())

    cursorObject.execute("USE db;")

    cr = Crawler()
    json_file = cr.start()

    insert_server_query(json_file['items'], cursorObject)
    insert_queue_query(json_file['items'], cursorObject)
    # cursorObject.execute(insert_server_query(json_file['items']))
    # cursorObject.execute(insert_queue_query(json_file['items']))

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    conn.close()