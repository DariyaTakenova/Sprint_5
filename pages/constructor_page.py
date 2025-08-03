from selenium.webdriver.support.ui import WebDriverWait
from locators import ConstructorLocators

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def go_to_buns(self):
        self.driver.find_element(*ConstructorLocators.BUNS_TAB).click()
        self.wait_for_active_tab("Булки")

    def go_to_sauces(self):
        self.driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
        self.wait_for_active_tab("Соусы")

    def go_to_fillings(self):
        self.driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()
        self.wait_for_active_tab("Начинки")

    def get_active_tab_text(self):
        return self.driver.find_element(*ConstructorLocators.ACTIVE_TAB).text

    def wait_for_active_tab(self, expected_text):
        self.wait.until(lambda d: self.get_active_tab_text() == expected_text)
