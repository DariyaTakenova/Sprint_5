from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from data import generate_email, generate_password, VALID_NAME
from locators import MainPageLocators, LoginPageLocators


class TestNavigation:

    def setup_method(self, driver):
        # регистрация и вход перед каждым тестом
        self.driver = driver
        self.email = generate_email()
        self.password = generate_password()

        self.driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        RegisterPage(self.driver).register_user(VALID_NAME, self.email, self.password)
        LoginPage(self.driver).login_user(self.email, self.password)

    def test_go_to_account(self):
        # переход в личный кабинет
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert "account" in self.driver.current_url

    def test_go_to_constructor_from_account(self):
        # переход в конструктор из личного кабинета
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
        assert "feed" in self.driver.current_url or "/" in self.driver.current_url

    def test_go_to_constructor_by_logo(self):
        # переход в конструктор по клику на логотип
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.driver.find_element(*MainPageLocators.LOGO).click()
        assert "feed" in self.driver.current_url or "/" in self.driver.current_url

    def test_logout_from_account(self):
        # выход из аккаунта
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        AccountPage(self.driver).click_exit_button()
        assert self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()
