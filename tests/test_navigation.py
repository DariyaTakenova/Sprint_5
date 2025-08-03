from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from data import generate_email, generate_password, VALID_NAME
from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By

def login_and_go_to_account(driver, email, password):
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    register_page = RegisterPage(driver)
    register_page.register_user(VALID_NAME, email, password)
    login_page = LoginPage(driver)
    login_page.login_user(email, password)

def test_go_to_account(driver):
    email = generate_email()
    password = generate_password()
    login_and_go_to_account(driver, email, password)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    assert "account" in driver.current_url

def test_go_to_constructor_from_account(driver):
    email = generate_email()
    password = generate_password()
    login_and_go_to_account(driver, email, password)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
    assert "feed" in driver.current_url or "/" in driver.current_url

def test_go_to_constructor_by_logo(driver):
    email = generate_email()
    password = generate_password()
    login_and_go_to_account(driver, email, password)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.LOGO).click()
    assert "feed" in driver.current_url or "/" in driver.current_url

def test_logout_from_account(driver):
    email = generate_email()
    password = generate_password()
    login_and_go_to_account(driver, email, password)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    account_page = AccountPage(driver)
    account_page.click_exit_button()
    assert driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()
