from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
