from selenium import webdriver
import unittest
import time
import xlrd


class moduleName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # define the path to the Excel file
        wb = xlrd.open_workbook('C://Github//python_testing_basics//DDT//data.xlsx')
        sheetname = wb.sheet_names()
        # Read for XLSX Sheet names
        sh1 = wb.sheet_by_index(0)

        i = 0
        while i < 3:
            rownum = i
            rows = sh1.row_values(rownum)
            element = driver.find_element_by_name("q")
            driver.find_element_by_name("q").send_keys(rows[0])
            element.submit()
            time.sleep(3)
            print "The keyword [" + rows[0] + "] is searched"
            driver.back()
            time.sleep(3)
            i = i + 1

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
