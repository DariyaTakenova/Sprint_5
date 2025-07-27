import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators

class TestAvatar:

    def clear_input(self, element):
        element.clear()

    def test_change_ava(self, revert_avatar, login):
        # Используем WebDriver, который возвращает фикстура login
        driver = login

        # Ждём прогрузки карточек
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.CARDS))

        # никогда не используем метод слипа
        time.sleep(1)

        # После полной загрузки аватара открываем окно редактирования аватара
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(Locators.PROFILE_IMAGE)
        ).click()

        # Ждём, пока появится поле ввода для URL аватара
        avatar_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.AVATAR_INPUT)
        )

        # Удаляем старое значение и добавляем новый URL аватара
        self.clear_input(avatar_input)
        avatar_input.send_keys(url_ava)

        # Нажимаем кнопку "Обновить"
        update_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.UPDATE_AVATAR_BUTTON)
        )
        update_button.click()

        # Убедимся, что новый аватар загрузился
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                Locators.PROFILE_IMAGE,
                "style",
                f'background-image: url("{url_ava}");'
            )
        )