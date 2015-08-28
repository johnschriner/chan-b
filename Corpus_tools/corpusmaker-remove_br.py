##python script to scrape a corpus from 4chan pages
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, NavigableString
import urllib2
import sys
import re
import time
from HTMLParser import HTMLParser
import htmlentitydefs



f = open("just_text.txt","a")
f.truncate()

#using beautiful soup
 
p = BeautifulSoup(open("all_merged.html"))

p = str(p).replace('<br>',' ')
p = str(p).replace('</br>',' ')


f.write(str(p))
f.close()
