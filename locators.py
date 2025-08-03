from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account' and .//p[text()='Личный Кабинет']]")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Добавить логотип
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")        # Добавить ссылку "Конструктор"

class LoginPageLocators:
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")  # Ссылка восстановление
    EMAIL_INPUT = (By.NAME, "email")  # Поле Email
    PASSWORD_INPUT = (By.NAME, "password")  # Поле пароль
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке

class AccountPageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")
