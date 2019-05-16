import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnLogin']").click()
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        self.driver.implicitly_wait(10)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/aarviaditya/Desktop/Testing/HTML_Python"),verbosity=2)

