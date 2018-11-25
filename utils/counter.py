#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 25.11.2018 10:56:13 MSK

import os
import re

names = ['bashgazet', 'bashdram', 'gsrb', 'jeshlek', 'kiskeufa', 'kulturarb', 'president-rb', 'tabin']


def main():
    wordcount = 0
    for folder in names:
        pth = 'texts-{}/'.format(folder)
        lst = os.listdir(pth)
        for fl in lst:
            with open(pth + fl) as f:
                c = f.read()
                words = c.split()
                for word in words:
                    if re.search('[а-яҙңҫүһғәҡөА-ЯҘҢҪҮҺҒӘҠӨ]', c):
                        wordcount += 1
    print(wordcount)
    return 0

if __name__ == '__main__':
    main()

