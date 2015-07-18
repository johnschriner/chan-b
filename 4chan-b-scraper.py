# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from datetime import timedelta
import unittest, time, re

class FromSeleniumForPython2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(45)
        self.base_url = "https://boards.4chan.org/b/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_from_selenium_for_python2(self):
        driver = self.driver
        driver.get("https://boards.4chan.org/b/")
        driver.find_element_by_xpath("(//img[@alt='+'])[1]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[2]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[3]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[4]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[6]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[7]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[8]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[9]").click()
        driver.find_element_by_xpath("(//img[@alt='+'])[10]").click()
        driver.implicitly_wait(20)
        elem = driver.find_element_by_xpath("//*")
        front_page = elem.get_attribute("outerHTML")
        f = open('front_page.html', 'w')
        f.write(front_page.encode('utf-8'))
        f.close
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
