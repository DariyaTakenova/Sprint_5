import pytest
from pages.login_page import LoginPage
from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By
from helper import register_user_for_login


@pytest.mark.usefixtures("new_user_credentials")
class TestLoginScenarios:

    def test_login_from_main_page(self, driver, new_user_credentials):
        email, password = new_user_credentials
        register_user_for_login(driver, email, password)

        # Нажимаем на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*MainPageLocators.LOGIN_MAIN_BUTTON).click()

        # Выполняем вход
        login_page = LoginPage(driver)
        login_page.login_user(email, password)

        # Проверяем, что вошли в личный кабинет
        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_from_personal_account_button(self, driver, new_user_credentials):
        email, password = new_user_credentials
        register_user_for_login(driver, email, password)

        # Нажимаем "Личный кабинет" в шапке
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        login_page = LoginPage(driver)
        login_page.login_user(email, password)

        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_from_register_page(self, driver, new_user_credentials):
        email, password = new_user_credentials
        register_user_for_login(driver, email, password)

        # Переходим в регистрацию, потом на вход
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(By.LINK_TEXT, "Войти").click()

        login_page = LoginPage(driver)
        login_page.login_user(email, password)

        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_from_forgot_password(self, driver, new_user_credentials):
        email, password = new_user_credentials
        register_user_for_login(driver, email, password)

        # Переходим в "Забыли пароль?", потом на вход
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(By.LINK_TEXT, "Войти").click()

        login_page = LoginPage(driver)
        login_page.login_user(email, password)

        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
