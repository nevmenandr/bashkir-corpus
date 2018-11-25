#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 25.11.2018 20:32:25 MSK

import os
import random
import re
import sys

PTH1 = sys.argv[1]
PTH2 = 'shuffled_texts/{}'.format(PTH1)
PATT = re.compile('([^А-ЯҘҢҪҮҺҒӘҠӨ][.?!] )|\n([А-ЯҘҢҪҮҺҒӘҠӨ])')

def main():
    lst = os.listdir(PTH1)
    for fl in lst:
        f = open('{}/{}'.format(PTH1, fl), 'r', encoding='utf-8')
        text = f.read()
        f.close()
        sents = PATT.sub(r'\1##&##\2', text)
        sents = sents.split('##&##')
        indexes = [x for x in range(len(sents))]
        random.shuffle(indexes)
        shuffled_text = []
        for indx in indexes:
            shuffled_text.append(sents[indx])
        with open('{}/{}'.format(PTH2, fl), 'w', encoding='utf-8') as fw:
            fw.write(' '.join(shuffled_text))
        

    
    return 0

if __name__ == '__main__':
    main()

