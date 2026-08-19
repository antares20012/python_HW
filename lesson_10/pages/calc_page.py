import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.ID, "delay")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver, url):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Открытие страницы калькулятора")
    def open_page(self):
        """
        Открывает страницу калькулятора.
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки {delay} секунд перед выводом результата")
    def set_delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        delay_input = self.wait.until(EC.element_to_be_clickable(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие на кнопку {button} калькуятора")
    def click_button(self, button):
        """
        Нажимает кнопку калькулютора
        :params button: str - Текст. написанный на кнопке калькулятора
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Нажатие на кнопки {buttons} калькулятора")
    def click_buttons(self, buttons):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: list[str] — список текстов на кнопках,
        которые нужно нажать.
        """
        for button in buttons:
            self.click_button(button)

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result, delay):
        """
        Ожидает появление ожидаемого результата на экране
        :params expected_result: str - ожидаемый результат вычислений
        :params delay: int - время через которое отобразится ожидаемый результат в секундах
        """
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
