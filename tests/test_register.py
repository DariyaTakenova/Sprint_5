from helper import generate_registration_data
from pages.register_page import RegistrationPage
# from curl import auth_endpoint  # ← подключение эндпоинта для дальнейших тестов

class TestRegistration:

    def test_success_registration(self, driver):
        # Arrange — создаём уникальные данные
        name, email, password = generate_registration_data()
        reg_page = RegistrationPage(driver)

        # Act — заполняем форму регистрации и отправляем
        reg_page.fill_registration_form(name, email, password)
        reg_page.submit()

        # Assert — если всё хорошо, произойдёт редирект на login
        assert "login" in driver.current_url
