__author__ = 'vygidor'

import unittest
from selenium import webdriver

class UITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #test will be performed in Chrome
        cls.driver = webdriver.Chrome()

    #open page in Chrome
    def test_1_title(self):
        self.driver.get('http://www.google.com')
        self.assertEqual(
            self.driver.title,
            'Google')

    # fill search field
    def test_2_searchbyname(self):
        self.driver.get('http://www.google.com')
        search_input = self.driver.find_element_by_name("q")
        search_input.send_keys("Python Selenium test driven testing")
        search_input.submit()

    # the same as test_2_searchbyname - the element will be defined by XPATH
    def test_3_searchbyxpath(self):
        self.driver.get('http://www.google.com')
        #search_input = self.driver.find_element_by_xpath('//*[@id="q"]') //*[@id="lst-ib"]
        search_input = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')
        search_input.send_keys("XPath")
        search_input.submit()

     # close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()