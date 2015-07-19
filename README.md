# 4chan-b
expands threads, scrapes, edits html for corpus linguistics usage

The purpose of this project is to scrape a forum for use in corpus linguistics research.
By looking at use of language (on an image board!) we can see trends (summer trends), topical discussion, repetitive themes, etc.

The html output is a balance of readability (for limited context) and ease of using in NLTK.  Some html tags are still present and can be edited from the html.

The shell script makes it easy to add as a cronjob and have timed scrapes on a headless machine.  This is ideal for a raspberry pi or something similar.

-------
You'll have to install Selenium's Webdriver library:  http://www.seleniumhq.org/download/
-------
Q:  Why not just use the API?  --->  https://github.com/4chan/4chan-API
A:  I wanted all text from the front page, not just the OP and recent activity in the thread.
-------

To do:

-Make monthly corpus

-Ability to convert to txt for NLTK

-Test on other sites with similar forum software


