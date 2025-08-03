import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def register_user_for_login(driver, email, password):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
    register_page = RegisterPage(driver)
    register_page.register_user(VALID_NAME, email, password)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))


@pytest.mark.usefixtures("new_user_credentials")
def test_login_from_main_page(driver, new_user_credentials):
    email, password = new_user_credentials
    register_user_for_login(driver, email, password)

    driver.find_element(*MainPageLocators.LOGIN_MAIN_BUTTON).click()

    login_page = LoginPage(driver)
    login_page.login_user(email, password)

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()


@pytest.mark.usefixtures("new_user_credentials")
def test_login_from_personal_account_button(driver, new_user_credentials):
    email, password = new_user_credentials
    register_user_for_login(driver, email, password)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    login_page = LoginPage(driver)
    login_page.login_user(email, password)

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()


@pytest.mark.usefixtures("new_user_credentials")
def test_login_from_register_page(driver, new_user_credentials):
    email, password = new_user_credentials
    register_user_for_login(driver, email, password)

    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    driver.find_element(By.LINK_TEXT, "Войти").click()

    login_page = LoginPage(driver)
    login_page.login_user(email, password)

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()


@pytest.mark.usefixtures("new_user_credentials")
def test_login_from_forgot_password(driver, new_user_credentials):
    email, password = new_user_credentials
    register_user_for_login(driver, email, password)

    driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
    driver.find_element(By.LINK_TEXT, "Войти").click()

    login_page = LoginPage(driver)
    login_page.login_user(email, password)

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
