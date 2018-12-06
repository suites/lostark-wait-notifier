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

from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

import requests
import platform
import config

class Crawler:
    def __init__(self, use_driver=True):
        if not use_driver:
            return

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        options.add_argument('no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        if platform.system() == "Linux":
            # chrome_path = r"/usr/lib/chromium-browser/chromedriver"
            chrome_path = config.CHROME_PATH['Linux']
        else:
            chrome_path = config.CHROME_PATH['Windows']

        self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)


    def start_notice(self):
        response = requests.get(config.URL_CONFIG['notice'])
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        links = soup.select('#list > div.list.list--default > ul:nth-of-type(2) > li > a')
        titles = soup.select('#list > div.list.list--default > ul:nth-of-type(2) > li > a > div.list__subject > span.list__title')

        notices = []
        for i in range(len(titles)):
            if '완료' in titles[i].text:
                continue

            url = "http://lostark.game.onstove.com" + links[i]['href']

            response = requests.get(url)
            html = response.text

            inner_soup = BeautifulSoup(html, 'html.parser')
            inner_title = inner_soup.find(text='[점검 시간]')
            if inner_title is None:
                continue

            inner_content = inner_title.parent.parent.findNext('p').contents[0].text

            notices.append([titles[i].text, inner_title + '\n' + inner_content, url])

        if len(notices) == 0:
            notices.append('예정된 점검 공지가 없습니다 😍')
        return notices


    def start_queue(self):
        url = config.URL_CONFIG['target']

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

