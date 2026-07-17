import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    # 1. Открытие страницы: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 55)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    # 2. Ввод в поле по локатору #delay  значение 45.
    set_delay = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#delay")
    ))
    set_delay.clear()
    set_delay.send_keys("45")
    # 3. Нажатие кнопок: "7" "+" "8" "="
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    # 4. Запуск таймера для подсчета секунд до появления результата
    start_time = time.time()
    # 5. Ожидание до появления результата
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    # 6. Остановка таймера
    end_time = time.time()
    # 7. Подсчет времени ожидания
    result = end_time - start_time
    # 8. Проверка времени ожидания
    assert result >= 45

    driver.quit()
