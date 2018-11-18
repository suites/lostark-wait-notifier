import requests
import json
from bs4 import BeautifulSoup

class Crawler:
    def start(self):
        response = requests.get('http://loaq.kr/')
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        servers = {}
        items = []

        servers['server_time'] = soup.select('div.time')[0].text.replace("  ","").replace('\n', '')
        print(servers['server_time'])

        server_name = ''

        for tag in soup.select('div.server-list'):
            server_name += tag.text

        server_name = server_name.replace(' ', '').split("\n")

        server_name = [x for x in server_name
                       if
                       "(" not in x and "상세" not in x and "서버" not in x and "대기열" not in x and "\xa0" not in x and "" != x]

        for i, item in enumerate(server_name):
            if i % 2 == 0:
                items.append({"server": item, "wait": server_name[i + 1]})

        servers["items"] = items

        # json_file = json.dumps(servers, indent=2, ensure_ascii=False)

        return servers