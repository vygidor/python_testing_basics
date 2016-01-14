from element import BasePageElement
from locators import MainPageLocators


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 's'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "TOOLSQA | Tutorials on Selenium, Java, TestNG, Cucumber, Spec Flow, Maven, IBATIS, Appium, Mobile AUtomation" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def submit_search_query(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        element.submit()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
