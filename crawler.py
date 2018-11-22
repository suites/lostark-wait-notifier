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

import platform
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

class Crawler:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        options.add_argument('no-sandbox')

        chrome_path = ''
        if platform.system() == "Linux":
            chrome_path = r"/usr/lib/chromium-browser/chromedriver"
            # chrome_path = r"chromedriver_linux64/chromedriver"
        else:
            chrome_path = r"chromedriver_win32/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

    def start(self):
        url = 'https://rubystarashe.github.io/lostark/'

        self.driver.get(url)
        sleep(1)
        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        servers = {}
        items = []

        now = datetime.now()
        servers['server_time'] = '%s-%s-%s %s시 %s분 기준' % (now.year, now.month, now.day, now.hour, now.minute)

        server_count = len(soup.select('span.data.name'))

        for i in range(server_count):
            server = soup.select('span.data.name')[i].text
            queue = soup.select('span.data.queue')[i].text
            if queue == '알 수 없음':
                queue = -1
            elif queue == '접속 가능':
                queue = 0
            items.append({"server": server, "queue": queue})

        servers["items"] = items

        return servers

    def end(self):
        self.driver.quit()

