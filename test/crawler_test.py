from modules.crawler import *

crawler = Crawler(use_driver=False)
notices = crawler.start_notice()
text = "🐤️로스트아크 점검 공지\n"
text += "═══════════\n"
for notice in notices:
    if type(notice) == str:
        text += notice + '\n\n'
    else:
        text += '\n\n'.join(notice)
    text += '\n\n-----------------------\n'

print(text)