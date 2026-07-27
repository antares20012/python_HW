import pytest
from selenium import webdriver
from pages.shop_page import ShopPage


@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):

    shop_page = ShopPage(driver, "https://www.saucedemo.com/")
    shop_page.open_page()
    shop_page.login_shop()
    shop_page.shopping()
    shop_page.checkout()
    shop_page.check_out_step_one()
    shop_page.check_out_step_two()
    total = shop_page.check_out_step_two()
    assert total == 58.29
