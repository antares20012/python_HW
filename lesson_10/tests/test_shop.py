import pytest
import allure
from selenium import webdriver
from pages.shop_page import ShopPage

EXPECTED_TOTAL = 58.29


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестированиние онлайн магазина")
@allure.description("Проверяет корректность работы функции расчета итоговой суммы при покупке товаров")
@allure.feature("Онлайн магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет корректность работы функции расчета итоговой суммы при покупке товаров.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """

    shop_page = ShopPage(driver, "https://www.saucedemo.com/")
    with allure.step("Открытие страницы магазина"):
        shop_page.open_page()
    with allure.step("Аутентификация пользователя в магазине"):
        shop_page.login_shop()
    with allure.step("Выбор товаров для покупки"):
        shop_page.shopping()
    with allure.step("Проверка товаров в корзине"):
        shop_page.checkout()
    with allure.step("Заполнение данных пользователя для отправки"):
        shop_page.check_out_step_one()
    with allure.step("Проверка конечной суммы стоимости товаров и результата"):
        total = shop_page.check_out_step_two()
        assert total == EXPECTED_TOTAL, f"Ожидалась сумма {EXPECTED_TOTAL}, но получили {total}"
