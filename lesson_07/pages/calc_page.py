import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    @staticmethod
    def get_button_locator(char: str) -> tuple:
        return By.XPATH, f"//span[text()='{char}']"


    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.wait = WebDriverWait(self.driver, 60)


    def open_page(self):
        self.driver.get(self.url)
        
    def set_delay(self):
        delay = self.wait.until(EC.element_to_be_clickable(
            self.DELAY_INPUT
        ))
        delay.clear()
        delay_count = 45
        delay.send_keys(str(delay_count))

    def calculate(self):
        self.driver.find_element(*CalcPage.get_button_locator("7")).click()
        self.driver.find_element(*CalcPage.get_button_locator("+")).click()
        self.driver.find_element(*CalcPage.get_button_locator("8")).click()
        start_time = time.time()
        self.driver.find_element(*CalcPage.get_button_locator("=")).click()
        self.wait.until(EC.text_to_be_present_in_element(self.SCREEN_RESULT, "15"))
        end_time = time.time()
        time_result = float(end_time - start_time)
        return time_result
