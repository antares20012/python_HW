from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    # 1. Открытие страницы: https://www.saucedemo.com/ в Firefox.
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 2. Авторизация
    print("\n1. Страница авторизации.")
    user_name = wait.until(EC.presence_of_element_located((
        By.ID, "user-name")
    ))
    user_name.send_keys("standard_user")
    wait.until(EC.text_to_be_present_in_element_value
               ((By.ID, "user-name"), "")
               )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров в корзину
    print("2. Добавление товаров в корзину.")
    backpack = wait.until(EC.presence_of_element_located(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    ))
    backpack.click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Переход в корзину
    print("3. Проверка товаров в корзине.")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 5. Нажатие Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполнение формы валидными данными
    print("4. Заполнение данных покупателя")
    first_name = wait.until(EC.presence_of_element_located(
        (By.ID, "first-name")
    ))
    first_name.send_keys("Андерсон")
    driver.find_element(By.ID, "last-name").send_keys("Томас")
    driver.find_element(By.ID, "postal-code").send_keys("60606")

    # 7. Нажатие кнопки Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Рассчет итоговой стоимости
    print("5. Расчет итоговой стоимости")
    wait.until(EC.url_contains("/checkout-step-two.html"))

    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    items_sum = 0.0

    for index, element in enumerate(price_elements, start=1):
        print(element.text)
        price_value = float(element.text.replace("$", ""))

        items_sum += price_value

    tax = 4.32
    calculated_sum = round((items_sum + tax), 2)
    print(f"Итоговая стоимость: ${calculated_sum}")
    total = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
    total_text = total.text
    total_clean = total_text.replace("Total: $", "").strip()
    total_value = float(total_clean)
    # 9. Проверка итоговой стоимости
    assert calculated_sum == total_value, f"Результаты не совпадают! Ожидали {calculated_sum}, получили {total_value}"

    # 10. Закрытие браузера
    driver.quit()
