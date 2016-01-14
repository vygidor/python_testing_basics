from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BUTTON = (By.CLASS_NAME, 'submit')
    SEARCH_INPUT = (By.NAME, 's')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
