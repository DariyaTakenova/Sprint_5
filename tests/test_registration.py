from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        email, password = generate_registration_data()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_POPUP)).text
        #assert
        assert reg_text == 'Вы успешно зарегистрировались'
        assert driver.current_url == main_site + 'signup'

class TestCheckingCreationExistingAccount:

    def test_failed_registration(self, driver):
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_POPUP)).text
        assert reg_text == 'Что-то пошло не так!\nПопробуйте ещё раз.'

