from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    #### Предварительные шаги
    #
    # Создано два аккаунта на https://gitflic.ru/.
    # login_1: 86e903244a@emailinbo.live    password_1: @@JUGg7-fXhFb8#     session_1:  Yzk3MzAyMzYtYmU4Mi00MmYxLTk2NzctYTQyOWI3ODk3MjQ2
    # login_2: 327e1a565b@emailinbo.live    password_2: sFQy.snR3*@a6EY     session_2:  MTMwOTk4YzYtM2YwOC00YWZjLTkyOGYtNjc5MGM0MmIwMjE1
    ##### Шаги
    #
    # 1. Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    # 2. Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "Yzk3MzAyMzYtYmU4Mi00MmYxLTk2NzctYTQyOWI3ODk3MjQ2",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # 3. Обновите страницу.
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/login_1_1")
    user_name_1 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "h6.mb-0")
    ))

    # 5. Сохраните текущий URL.
    url_1 = driver.current_url
    print(url_1)

    # 6. Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()
    driver.get("https://gitflic.ru/")

    # 7. Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "MTMwOTk4YzYtM2YwOC00YWZjLTkyOGYtNjc5MGM0MmIwMjE1",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # 8. Обновите страницу.
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/login_2_2")
    user_name_2 = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "h6.mb-0")
    ))

    # 10. Сохраните текущий URL.
    url_2 = driver.current_url
    print(url_2)

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_1 != url_2

    driver.quit()