from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    # 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html в Edge
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    # 2. Очистка полей перед заполненеим
    inputs = driver.find_elements(By.TAG_NAME, "input")

    for input in inputs:
        if input.is_displayed() and input.is_enabled():
            input.clear()
    # 3. Заполнение полей
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "city": "Москва",
        "country": "Россия",
        "zip-code": "",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for field_name, value in form_data.items():

        locator = f"input[name='{field_name}']"
        driver.find_element(By.CSS_SELECTOR, locator).send_keys(value)

    # 4. Проверка, что поле "zip-code" пустое
    zipcode = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zipcode.clear()
    # 5. Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # 6. Ожидание пока на странице не появятся обновленные элементы
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.alert')))
    # 7. Поиск подкрашенных полей
    green_fields = driver.find_elements(By.CSS_SELECTOR, ".alert.py-2.alert-success")
    red_fields = driver.find_elements(By.CSS_SELECTOR, ".alert.py-2.alert-danger")
    # 8. Проверка заполнения полей
    for field in red_fields:
        assert "alert-danger" in field.get_attribute("class"), f"поле {field.text} надо заполнить"
    for field in green_fields:
        assert "alert-success" in field.get_attribute("class"), f"{field.text} заполнено"

    driver.quit()
