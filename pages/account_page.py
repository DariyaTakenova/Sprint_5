from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AccountPageLocators

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_exit_button(self):
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)).click()
