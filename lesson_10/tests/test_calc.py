import pytest
import allure
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера в браузере Google Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 1),
        ("9", "-", "3", "6", 1),
        ("4", "x", "5", "20", 1),
        ("8", "÷", "2", "4", 1),
    ],
)
@allure.title("Тестироение калькулятора {num1} {operation} {num2} "
              "= {expected_result}")
@allure.description("Проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver, num1, operation,
                         num2, expected_result, delay):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+, -, x, ÷).
    :param num2: str — второе число для операции.
    :param expected_result: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    main_page = CalcPage(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    with allure.step("Открытие страницы калькулятора"):
        main_page.open_page()
    with allure.step(f"Установка задержки {delay} перед выводом резулььтата"):
        main_page.set_delay(delay)
    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, '='"):
        main_page.click_buttons([num1, operation, num2, "="])
    with allure.step(f"Ожидание результата {expected_result}"):
        main_page.wait_for_result(expected_result, delay)
    with allure.step(f"Проверка результата {expected_result}"):
        assert main_page.get_result() == expected_result, \
            f"Expected result:{expected_result}, but got:{main_page.get_result()}"
