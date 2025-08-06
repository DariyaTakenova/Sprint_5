from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from pages.register_page import RegisterPage
from data import VALID_NAME

def register_user_for_login(driver, email, password):

    # Переход на страницу логина
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Нажимаем Зарегистрироваться
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
    ).click()

    # Создаём страницу регистрации и регистрируемся
    register_page = RegisterPage(driver)
    register_page.register_user(VALID_NAME, email, password)

    # Ждём появления поля email на странице входа
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
