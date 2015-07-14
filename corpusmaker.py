##python script to scrape a corpus from 4chan pages
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, NavigableString
import urllib2
import sys
import re
import time
from HTMLParser import HTMLParser
import htmlentitydefs
if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")



sys.setrecursionlimit(2000)
timestr = time.strftime("%Y%m%d-%H%M") 
f = open("htmlfiles/" + timestr + "-b.html","a")
f.truncate()

#using beautiful soup
 
soup = BeautifulSoup(open("front_page.html"))
for div in soup.findAll('a','quotelink'):
    div.extract()

p = soup.prettify()
p = soup.find_all("blockquote")


p = str(p).replace('<blockquote class="postMessage" ',' ')
p = str(p).replace('<a data-cmd="embed" data-type="yt" href="javascript:;">Embed</a>',' ')
p = str(p).replace('</blockquote>, ',' ')
p = str(p).replace('<span class="quote">&gt;',' ')
p = str(p).replace('</span>',' ')
p = str(p).replace('<s>',' ')
p = str(p).replace('</s>',' ')
#p = str(p).replace('<br>',' ')
#p = str(p).replace('</br>',' ')
p = re.sub(ur' id=.............',' ', p)

f.write(str(p))
f.close()