from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #1. Открытие страницы https://httpbin.org/
    driver.get("https://httpbin.org/")
    sleep(2)
    #2. Поиск и нажатие на ссылку HTML Form.
    a_href = driver.find_element(By.LINK_TEXT, "HTML form")
    a_href.click()
    sleep(3)
    #3. Проверка, изменения URL на /forms/post
    assert driver.current_url == "https://httpbin.org/forms/post"
    #4. Переход на домашнюю страницу
    driver.back()
    sleep(2)
    #5. Проверка URL текущей страницы
    assert driver.current_url == "https://httpbin.org/"
    sleep(2)
    driver.quit()
