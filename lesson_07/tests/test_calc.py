import pytest
from selenium import webdriver
from pages.calc_page import CalcPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_calc(driver):
    calc_page = CalcPage(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calc_page.open_page()
    calc_page.set_delay()
    time_result = calc_page.calculate()
    assert time_result >= 45
