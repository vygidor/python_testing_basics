__author__ = 'vygidor'

import unittest
from selenium import webdriver

class UITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox() #test will be performed in Firefox

#open page in browser
    def test_title(google):
        google.driver.get('http://www.google.com')
        google.assertEqual(
            google.driver.title,
            'Google')

#here comes the magic :)

#close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()