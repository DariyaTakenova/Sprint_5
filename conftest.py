import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
    options.add_argument("--window-size=1200,600")
    service = Service("/Users/kg-bulatov/yandexdriver14")
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    # Вводим email в поле "Email"
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    return driver

@pytest.fixture()
def revert_avatar():
    # Учётные данные пользователя
    credentials = {
        "email": Credentials.email,
        "password": Credentials.password,
    }

    # Авторизация
    response = requests.post(auth_endpoint, json=credentials)
    token = response.json().get("token")

    # Обновление аватара
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    update_data = {
        "avatar": default_ava_url,
    }
    requests.patch(avatar_update_endpoint, json=update_data, headers=headers)

    yield