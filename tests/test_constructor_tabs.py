import pytest
from pages.constructor_page import ConstructorPage

@pytest.mark.parametrize("tab_method, expected_text", [
    ("go_to_buns", "Булки"),
    ("go_to_sauces", "Соусы"),
    ("go_to_fillings", "Начинки"),
])
def test_switch_constructor_tabs(driver, tab_method, expected_text):
    constructor_page = ConstructorPage(driver)

    # Уйдём на другую вкладку перед проверкой "Булки"
    if tab_method == "go_to_buns":
        constructor_page.go_to_fillings()

    # Вызов нужного метода перехода
    getattr(constructor_page, tab_method)()

    # Проверка активной вкладки
    assert constructor_page.get_active_tab_text() == expected_text
