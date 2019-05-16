import unittest
import HtmlTestRunner
from selenium import webdriver
from OrangeHRM_Code.Rough_code import Homepage
from OrangeHRM_Code.Rough_code import Loginpage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = Loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()






    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/aarviaditya/Desktop/Testing/HTML_Python"),verbosity=2)




