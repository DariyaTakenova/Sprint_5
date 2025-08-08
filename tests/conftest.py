import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data import generate_email, generate_password, VALID_NAME
from curl import MAIN_SITE
from locators import LoginPageLocators
from pages.register_page import RegisterPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    driver.get(MAIN_SITE)
    yield driver
    driver.quit()


@pytest.fixture
def new_user_credentials():
    email = generate_email()
    password = generate_password()
    return email, password


@pytest.fixture
def register_user_for_login(driver):
    def _register(email, password):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        register_page = RegisterPage(driver)
        register_page.register_user(VALID_NAME, email, password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))  # Убедиться, что попали на логин
    return _register
