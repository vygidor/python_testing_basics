__author__ = 'vygidor'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# for Safari you have to install Safari Webdriver extension into your Safari browser
# note: for a working extension you need to get a proper certificate from Apple developer program
#
# also you need to download Selenium standalone JAR: http://docs.seleniumhq.org/download/
# put the JAR file in the same folder as your .PY file
# define the 'SELENIUM_SERVER_JAR' via os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.46.0.jar"
# note: your version may be different

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.46.0.jar"
# if you want to pass the VM arguments and write debug of Selenium in a new file:
# java -jar -D selenium.LOGGER=log.txt selenium-server-standalone-2.46.0.jar

driver = webdriver.Safari()

driver.implicitly_wait(10)
driver.get('http://www.google.com/')
assert "Google" in driver.title

elem = driver.find_element_by_name('q')
elem.send_keys('Selenium')
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()