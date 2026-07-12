from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dinamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()
    # 2. Найдите и нажмите на кнопку Start.
    btn_start = driver.find_element(By.CSS_SELECTOR, 'div[id="start"] button')
    btn_start.click()
    # 3. Дождитесь появления текста Hello World!
    text_on_page = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div[id='finish'] h4")
    ))
    # 4. Сделайте скриншот страницы.
    driver.save_screenshot('screenshot.png')
    # 5. Проверьте, что появившийся текст равен Hello World!
    assert "Hello World!" in text_on_page.text
    driver.quit()
