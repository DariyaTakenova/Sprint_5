from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
from selenium.common.exceptions import TimeoutException

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_name(self, name):
        self.driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    def register_user(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()

    def get_error_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)).text
        except TimeoutException:
            return None
