from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    # 1.	Открытие страницы https://httpbin.org/links/10.
    driver.get("https://httpbin.org/links/10")
    # 2.	Поиск всех ссылок на странице (тег <a>).
    links = driver.find_elements(By.XPATH, "//a[@href]")
    count = len(links)
    print(f"Количество ссылок на странице: {count}")
    # 3.	Проверка, количества ссылок (9).
    assert count == 9
    # 4.	Проверка отображения ссылок на странице.
    for link in links:
        assert link.is_displayed() is True
    # 5.	Проверьте, что текст первой ссылки содержит "1".
    first_link = links[0].text
    assert "1" in first_link

    driver.quit()
