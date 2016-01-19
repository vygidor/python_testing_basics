import unittest
from datetime import datetime  # to support the screenshot feature
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class UITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # test will be performed in Chrome
        cls.driver = webdriver.Chrome()

    # open page in Chrome
    def test_1_title(self):
        self.driver.get('http://www.google.com')
        self.assertEqual(
            self.driver.title,
            'Google')

    # fill search field
    def test_2_search_by_name(self):
        # the code was improved to show how the screenshot-on-error functionality can be used in the test case
        try:
            self.driver.get('http://www.google.com2')
            search_input = self.driver.find_element_by_name("q")
            search_input.send_keys("Python Selenium test driven testing")
            search_input.submit()
        except Exception as e:
            print e
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('screenshot-%s.png' % now)

    # the same as test_2_searchbyname - the element will be defined by XPATH
    def test_3_search_by_xpath(self):
        self.driver.get('http://www.google.com')
        # search_input = self.driver.find_element_by_xpath('//*[@id="q"]') //*[@id="lst-ib"]
        search_input = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')
        search_input.send_keys("XPath")
        search_input.submit()

    # will wait until the element is loaded but not longer as defined in variable
    # Note: you have to extend your imports:
    # from selenium.webdriver.support.ui import WebDriverWait
    #       from selenium.webdriver.support import expected_conditions as EC
    #       from selenium.webdriver.common.by import By
    #       from selenium.common.exceptions import TimeoutException
    def test_4_wait_until_loaded(self):
        self.driver.get('http://www.google.com')
        # seconds to wait for the element to appear
        delay = 20
        try:
            WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.ID, 'hplogo')))
            print "Loading successful!"
        except TimeoutException:
            print "Loading took too much time!"

    # will wait until the element is clickable (available to click) but not longer as defined in WebDriverWait
    # (for this example it is 20 seconds)
    def test_5_wait_until_clickable(self):
        self.driver.get('http://toolsqa.com')
        try:
            WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main-nav"]/li[2]/a')))
        except TimeoutException:
            print "'Tutorials' button not available!"

    # close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
