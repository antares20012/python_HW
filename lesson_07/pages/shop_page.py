from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    @staticmethod
    def get_button_locator(char: str) -> tuple:
        return By.ID, f"add-to-cart-sauce-labs-{char}"

    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    SHOPPING_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CARD = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def __init__(self, driver, url):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.saucedemo.com/"

    def open_page(self):
        self.driver.get(self.url)

    def login_shop(self):
        user_name = self.wait.until(EC.presence_of_element_located(
            self.USER_NAME
        ))
        user_name.send_keys("standard_user")

        password = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD
        ))
        password.send_keys("secret_sauce")

        login_button = self.wait.until(EC.element_to_be_clickable(
            self.LOGIN_BUTTON
        ))
        login_button.click()

    def shopping(self):
        items = ["backpack", "bolt-t-shirt", "onesie"]
        for item in items:
            locator = ShopPage.get_button_locator(item)
            self.driver.find_element(*locator).click()

        shopping_card = self.wait.until(EC.presence_of_element_located(
            self.SHOPPING_CARD))
        shopping_card.click()

    def checkout(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        checkout_button = self.wait.until(EC.presence_of_element_located(
            self.CHECKOUT
        ))
        checkout_button.click()

    def check_out_step_one(self):
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME
        ))
        user_data = {
            "first-name": "Бэггинс",
            "last-name": "Бильбо",
            "postal-code": "12345"
        }

        for field_name, value in user_data.items():
            locator = (By.CSS_SELECTOR, f"#{field_name}")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)

        continue_btn = self.wait.until(EC.element_to_be_clickable(
            self.CONTINUE_BTN
        ))
        continue_btn.click()

    def check_out_step_two(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        items_sum = 0.0
        for index, element in enumerate(price_elements, start=1):
            print(element.text)
            price_value = float(element.text.replace("$", ""))

            items_sum += price_value
        tax_rate = 0.08
        tax = tax_rate * items_sum
        calculated_sum = round((items_sum + tax), 2)
        print(f"Итоговая стоимость: ${calculated_sum}")
        return calculated_sum
