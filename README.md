# Python automation testing basics
Understanding the basics with data driven UI testing with Python, [Selenium](https://pypi.python.org/pypi/selenium) &amp; [nose](https://nose.readthedocs.org/en/latest/) / [unittest](https://docs.python.org/2/library/unittest.html).

Note: '[nose](https://nose.readthedocs.org/en/latest/)' is used only for standalone execution. As I use PyCharm with '[pydev](https://www.jetbrains.com/pycharm/help/remote-debugging.html)' support for debugging and '[unittest](https://docs.python.org/2/library/unittest.html)' module for running the tests, I am actually not using it.

For DDT you have to install '[ddt](https://ddt.readthedocs.org/en/latest/index.html)'.

## Automated unit tests
A testcase is created by subclassing `unittest.TestCase`. The individual tests are defined with methods whose names start with the letters `test`. This naming convention informs the test runner about which methods represent tests. (see *ui_test_basics.py*)
The `setUp()` and `tearDown()` methods allow you to define instructions that will be executed before and after each test method.

## Other Automated tests
Files *ui_test_basics2.py*, *ui_test_basics3.py* and *ui_test_basics4.py* are basic .py scripts demonstrating the ability to build the automated test framework with Selenium Webdriver and Python. All except *ui_test_basics4.py* are using Firefox browser.

##Using Safari browser
When you simply try to run a test using `webdriver.Safari()` you will get an `SELENIUM_SERVER_JAR` message.
I found several solutions for running Selenium Webdriver with Python bindings on Safari browser but none of them worked for me.
It should be easy. First, you need valid certificate from Apple. And yes, that's a major stop for me. Apple merged his Safari Developer Program with other one(s) and created Apple Developer Program which costs 99 USD per membership year. So a showstopper for me. If you have it, continue.  
Second, you need to download '[Selenium Standalone Server](http://www.seleniumhq.org/download/)' and put it somewhere (I put it in the same directory as my python script). Then you are able to set the `SELENIUM_SERVER_JAR` variable:  
`os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.46.0.jar"`  
Don't forget to `import os`.  
Third, you need to install an extension into Safari. You can use downloaded .JAR file, copy it to a directory of your choice, run `jar xf selenium-server-standalone-2.46.0.jar` (the filename can be different in your case) and navigate to `org/openqa/selenium/safari` where *SafariDriver.safariextz* is located. Just install & activate it (Open Safari -> Preferences -> Extensions (tab)).

Note: if you have a solution for Safari 8 on Yosemite (10.10.X) which is working, pls share it with me.  
Note #2: there is a brew formula `selenium-server-standalone` which can be installed instead of downloading .JAR file.

##Using Chrome
Before you run a python file *ui_test_basics5.py* it is good to read 'Chromedriver - Getting Started(https://sites.google.com/a/chromium.org/chromedriver/getting-started)' to find out how to configure the script to get chromedriver executable to work (best choice for MAC OS X is to download it to /usr/bin) and setup the PATH so you don;t get any kind of error).

Comming soon:
- cross-browser script

Credits:
- http://selenium-python.readthedocs.org/en/latest/index.html
- http://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/
- https://code.google.com/p/selenium/wiki/PythonBindings
- http://scrolltest.com/selenium-testcase-with-nose-in-python/
- http://scrolltest.com/selenium-test-case-using-data-driven-testing-in-python/
- http://seleniummaster.com/sitecontent/index.php/selenium-web-driver-menu/selenium-test-automation-with-python-menu/188-python-selenium-web-driver-data-driven-framework
- https://docs.python.org/2/library/unittest.html
- https://code.google.com/p/selenium/wiki/SafariDriver
- https://blog.codecentric.de/en/2015/02/selenium-webdriver-safari-8/
- http://damien.co/resources/how-to-get-started-selenium-2-mac-os-x-java-7403
- https://sites.google.com/a/chromium.org/chromedriver/home