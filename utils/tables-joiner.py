#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 25.11.2018 20:25:03 MSK

names = ['bashgazet', 'bashdram', 'gsrb', 'jeshlek', 'kiskeufa', 'kulturarb', 'president-rb', 'tabin']

def main():
    fm = open('non_free_metatable.tsv', 'w', encoding='utf-8')
    fm.write('path	author	title	year	place	edition	gender	genre	source\n')
    for name in names:
        f = open(name + '_metatable.tsv')
        for i, line in enumerate(f):
            if i:
                fm.write(line)
    fm.close()
    
    return 0

if __name__ == '__main__':
    main()

