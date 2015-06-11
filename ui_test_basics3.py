__author__ = 'vygidor'

# code from http://selenium-python.readthedocs.org/en/latest/getting-started.html
# code rewritten to work with google.com
# level: code monkey

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("Selenium")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
