import unittest
from selenium import webdriver
import page


class Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.toolsqa.com")

    def test_search_the_page(self):
        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "toolsqa.com title doesn't match."
        # Sets the text of search textbox to "python"
        main_page.click_search_button()
        main_page.search_text_element = "python"
        # Submits the search query
        main_page.submit_search_query()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
