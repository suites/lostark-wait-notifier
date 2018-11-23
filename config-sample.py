# -*- coding: utf-8 -*-

# Database config 입니다.
# Example :
# 'host': 'localhost',
# 'db': 'db',
# 'user': 'root',
# 'password': '1234'
# 'charset': 'utf8'
DATABASE_CONFIG = {
    'host': '{host}',
    'db': '{db}',
    'user': '{user}',
    'password': '{password}',
    'charset': 'utf8'
}

# Chrome driver의 path입니다.
# Example : chromedriver_linux64/chromedriver
CHROME_PATH = {
    'linux': r"your/path/chromedriver",
    'Windows': r"your/path/chromedriver.exe",
}

# 크롤링 대상 url입니다.
# Example : https://rubystarashe.github.io/lostark/
TARGET_URL = 'https://rubystarashe.github.io/lostark/'

# Server config
# Example :
# 'host': '0.0.0.0',
# 'port': '8080'
SERVER_CONFIG = {
    'host': '0.0.0.0',
    'port': 8080
}