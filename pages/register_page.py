from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_registration_form(self, name, email, password):
        self.driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*RegistrationLocators.ERROR_MESSAGE).text
