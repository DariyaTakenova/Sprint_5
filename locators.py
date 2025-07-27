from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    REG_BUTTON = [By.XPATH, "//a[@class='header__auth-link']"]
    REG_POPUP = (By.XPATH, "//p[@class='popup__status-message']")
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    REGISTER_BUTTON = By.XPATH, "//button[@class='auth-form__button']"

    # Локаторы для изменения аватара
    PROFILE_IMAGE = (By.XPATH, "//div[@class='profile__image']")
    AVATAR_INPUT = (By.ID, "owner-avatar")
    UPDATE_AVATAR_BUTTON = (By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']")
    CARDS = (By.CLASS_NAME, "card__image")