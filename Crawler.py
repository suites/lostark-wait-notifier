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
from selenium import webdriver
import json
import os.path


class Crawler:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        self.driver = webdriver.Chrome(executable_path=r"chromedriver_win32/chromedriver.exe", chrome_options=options)
        self.url = ''
        print('프로그램 초기화 성공!')

    def start(self, url):
        self.url = url

        self.driver.get(self.url)
        print('접속 성공!')

        servers = {}
        items = []

        servers['server_time'] = self.driver.find_element_by_css_selector('div.time').text

        server_name = self.driver.find_element_by_css_selector('div.server-list').text
        server_name = server_name.replace(' ', '').split("\n")

        server_name = [x for x in server_name if "(" not in x and "상세" not in x and "서버" not in x and "대기열" not in x]

        for i, item in enumerate(server_name):
            if i % 2 == 0:
                items.append({"server": item, "wait": server_name[i + 1]})

        servers["items"] = items

        json_file = json.dumps(servers, indent=2, ensure_ascii=False)

        self.driver.close()
        return servers


