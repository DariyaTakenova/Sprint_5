import pytest
from pages.constructor_page import ConstructorPage

# Класс для тестов переключения вкладок конструктора
class TestConstructorTabs:

    def test_switch_to_buns(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_fillings()

        # Переход на вкладку "Булки"
        constructor_page.go_to_buns()

        # Проверяем, что вкладка "Булки" активна
        assert constructor_page.get_active_tab_text() == "Булки"

    def test_switch_to_sauces(self, driver):
        constructor_page = ConstructorPage(driver)

        # Переход на вкладку "Соусы"
        constructor_page.go_to_sauces()

        # Проверяем, что вкладка "Соусы" активна
        assert constructor_page.get_active_tab_text() == "Соусы"

    def test_switch_to_fillings(self, driver):
        constructor_page = ConstructorPage(driver)

        # Переход на вкладку "Начинки"
        constructor_page.go_to_fillings()

        # Проверяем, что вкладка "Начинки" активна
        assert constructor_page.get_active_tab_text() == "Начинки"
