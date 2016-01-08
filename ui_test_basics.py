__author__ = 'vygidor'

import unittest
from selenium import webdriver

class UITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # test will be performed in Firefox
        cls.driver = webdriver.Firefox()

    # open page in browser
    def test_1_title(self):
        self.driver.get('https://www.google.com')
        self.assertEqual(
            self.driver.title,
            'Google')

    # here comes the magic :)

    # fill search field
    def test_2_search(self):
        self.driver.get('https://www.google.com')
        search_input = self.driver.find_element_by_name("q")
        search_input.send_keys("Python Selenium test driven testing")
        search_input.submit()

    # close the browser window
    # @classmethod
    # def tearDownClass(cls):
    #   cls.driver.quit()