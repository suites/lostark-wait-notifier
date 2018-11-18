# -*- coding: utf-8 -*-

import re
import sys
from Crawler import *

if __name__ == "__main__":
    cr = Crawler()

    url = "http://loaq.kr/"
    cr.start(url)
