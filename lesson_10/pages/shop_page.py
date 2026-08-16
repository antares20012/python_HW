import allure
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
        """
        Конструктор класса ShopPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открытие страницы магазина")
    def open_page(self):
        """
        Открывает страницу онлайн магазина.
        """
        self.driver.get(self.url)

    @allure.step("Аутентификация пользователя в магазине")
    def login_shop(self, username: str = "standard_user", password: str = "secret_sauce") -> None:
        """
        Функция выполняет вход пользователя на сайт онлайн магазина
        :username: str - имя пользователя
        :password: str - пользовательсктй пароль
        """

        with allure.step(f"Ввод имени пользователя: {username}"):
            user_field = self.wait.until(EC.presence_of_element_located(self.USER_NAME))
            user_field.clear()
            user_field.send_keys(username)

        with allure.step(f"Ввод пароля: {'*' * len(password)}"):  # в отчёте не показываем пароль целиком
            pass_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD))
            pass_field.clear()
            pass_field.send_keys(password)

        with allure.step("Клик по кнопке входа"):
            login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
            login_button.click()

    @allure.step("Добавление товаров в корзину")
    def shopping(self, items = None):
        """
        Функция добавляет выбранные товары в корзину.
        """
        if items is None:
            items = ["backpack", "bolt-t-shirt", "onesie"]
        with allure.step("Клик по каждому выбранному товару"):
            for item in items:
                locator = self.get_button_locator(item)
                button = self.wait.until(EC.element_to_be_clickable(locator))
                button.click()

            shopping_card = self.wait.until(EC.presence_of_element_located(
                self.SHOPPING_CARD))
            shopping_card.click()

    @allure.step("Проверка налчия товаров в корзине")
    def checkout(self):
        """
        Функция проверяет наличие выбранных товаров в корзине.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        checkout_button = self.wait.until(EC.presence_of_element_located(
            self.CHECKOUT
        ))
        checkout_button.click()

    @allure.step(
        "Заполнение данных пользователя для отправки (Имя: {first_name}, Фамилия: {last_name}, Индекс: {postal_code})")
    def check_out_step_one(self, first_name: str = "Бэггинс", last_name: str = "Бильбо", postal_code: str = "12345"):
        """
        Функция заполняет данные аутентифицированного пользователя для отправки.
        :first-name: str - Имя, используемое для доставки
        :last-name: str - Фамилия, используемая для доставки
        :postal-code: str - почтовый индкс места доставки
        """
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

        user_data = {
            "first-name": first_name,
            "last-name": last_name,
            "postal-code": postal_code
        }
        for field_name, value in user_data.items():
            with allure.step(f"Ввод в поле '{field_name}': {value}"):
                locator = (By.CSS_SELECTOR, f"#{field_name}")
                element = self.wait.until(EC.visibility_of_element_located(locator))
                element.clear()
                element.send_keys(value)

        with allure.step("Нажатие кнопки для продолжения оформления покупок"):
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            continue_btn.click()

    @allure.step("Проверка итоговой суммы для оплаты с учетом налога")
    def check_out_step_two(self):
        """
        Функция проверяет итоговую сумму для оплаты с учетом налога.
        :return: float - рассчитанная сумма всех покупок с точностью до 2х знаков
        """
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        items_sum = 0.0
        with allure.step("Рассчет стоимости всех товаров"):
            for index, element in enumerate(price_elements, start=1):
                print(element.text)
                price_value = float(element.text.replace("$", ""))
                items_sum += price_value
                allure.attach(f"Товар {index}: ${price_value}", name=f"Цена товара {index}", attachment_type=allure.attachment_type.TEXT)
        with allure.step("Рассчет стоимости всех товаров с учетом налогов"):
            tax_rate = 0.08
            tax = tax_rate * items_sum
            calculated_sum = round((items_sum + tax), 2)
            allure.attach(f"Итоговая стоимость: ${calculated_sum}", name="Результат расчета", attachment_type=allure.attachment_type.TEXT)
            print(f"Итоговая стоимость: ${calculated_sum}")
        return calculated_sum
