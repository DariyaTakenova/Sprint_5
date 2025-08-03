from pages.register_page import RegisterPage
from locators import LoginPageLocators
from data import generate_email, generate_password, INVALID_PASSWORD, VALID_NAME

def test_successful_registration(driver):
    # Переход на форму регистрации
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    register_page = RegisterPage(driver)
    email = generate_email()
    password = generate_password()

    register_page.register_user(VALID_NAME, email, password)

    # Проверка: после регистрации мы попали на форму входа (кнопка "Войти" видна)
    assert driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()


def test_registration_with_invalid_password(driver):
    # Переход на форму регистрации
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    register_page = RegisterPage(driver)
    email = generate_email()

    register_page.register_user(VALID_NAME, email, INVALID_PASSWORD)

    # Проверка текста ошибки
    error = register_page.get_error_message()
    assert error == "Некорректный пароль"
