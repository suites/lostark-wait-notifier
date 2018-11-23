from modules.crawler import *

cr = Crawler(use_driver = False)

notices = cr.start_notice()
notices += cr.start_notice()

text = ''
for notice in notices:
    text += '\n'.join(notice)
    text += '\n\n=============================\n'


print(text)