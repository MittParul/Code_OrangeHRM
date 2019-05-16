class Homepage():

    def __init__(self, driver):
        self.driver = driver
        # these are 3 locators on this page
        self.welcome_button_xpath = "//a[@id='welcome']"
        self.logout_button_xpath = "//a[contains(text(),'Logout')]"

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_button_xpath).click()


    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
