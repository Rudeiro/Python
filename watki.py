#!/usr/bin/env python3
# coding: utf8 albo # -*- coding: utf-8 -*-
import re
import html.parser
import urllib.request
import threading
import time
class MyHTMLParser(html.parser.HTMLParser):
    dep = 0
    sit = []
    vis = []
    maxd = 0
    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            for (atr, val) in attrs:
                if atr == 'href':
                    if val.startswith('http') and val not in self.vis and self.dep <= self.maxd:
                        self.sit.append((val, self.dep))
                        self.vis.append(val)

class T(threading.Thread):
    def __init__(self, s):
        self.strona = s
        threading.Thread.__init__(self)
        with urllib.request.urlopen(self.strona[0]) as data:
            self.k = str(data.read())
    def run(self):
        MyHTMLParser().feed(self.k)
    def gle(self):
        return self.strona[1]
    def sprawdz(self):
        if re.search('basen', self.k):
            print('cos')
class Iterator(object):
    def __init__(self, site, maxd):
        MyHTMLParser.sit.append((site, 0))
        MyHTMLParser.vis.append(site)
        MyHTMLParser.maxd = maxd

    def __iter__(self):
        return self

    def __next__(self):

        #if len(MyHTMLParser.sit) == 0:
            #raise StopIteration()
        while True:
            if len(MyHTMLParser.sit) != 0:
                break

        site = T(MyHTMLParser.sit[0])
        MyHTMLParser.dep = site.gle() + 1
        site.start()
        site.sprawdz()

        x = MyHTMLParser.sit[0]
        MyHTMLParser.sit = MyHTMLParser.sit[1:]

        return x

if __name__ == "__main__":
    xd = Iterator('http://lo14.wroc.pl/',2)
    #print(len(MyHTMLParser.sit))
    for i in xd:
        print(i)
        print(len(MyHTMLParser.sit))

    print(len(MyHTMLParser.sit))
