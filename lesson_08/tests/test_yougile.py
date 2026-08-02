from pages.yougile_page import YougileApi


def test_yougile_positive(credentials):
    yougile_page = YougileApi("https://ru.yougile.com/api-v2", credentials=credentials)

    # 1. Получение ID компании
    company_id = yougile_page.get_yougile_my_company_id()
    print(f"ID Вашей компании {company_id}")
    assert company_id is not None, "Не удалось получить ID компании"
    assert yougile_page.last_status_code == 200, f"Ожидали статус 200, получили {yougile_page.last_status_code}"

    # 2. Создание API-ключа
    token = yougile_page.create_yougile_my_key()
    print(token)
    assert token is not None, "API-ключ не был сгенерирован"
    assert yougile_page.last_status_code in [200, 201], f"Неверный статус-код: {yougile_page.last_status_code}"

    # 3. Получение сохраненного ключа
    fetched_key = yougile_page.get_yougile_my_key()
    print(fetched_key)
    assert fetched_key is not None, "Не удалось запросить текущие API-ключи"
    assert yougile_page.last_status_code in [200, 201], f"Неверный статус-код: {yougile_page.last_status_code}"

    # 4. Создание проекта
    target_title = "QA Automation Project"
    project_data = yougile_page.create_project(title=target_title)
    assert isinstance(project_data, dict), f"Ожидался словарь, получен {type(project_data)}"
    assert project_data.get("id") is not None, "Проект не был создан"
    assert yougile_page.last_status_code in [200, 201], f"Статус-код: {yougile_page.last_status_code}"

    # 5. Проверка имени созданного проекта
    current_title = yougile_page.get_last_project_title()
    assert current_title == target_title, f"Ожидалось имя '{target_title}', получили '{current_title}'"

    # 6. Обновление проекта
    updated_title = "QA Automation Project - Updated"
    update_res = yougile_page.update_project(new_title=updated_title)
    assert update_res is not None, "Сервер вернул пустой ответ при обновлении проекта"
    assert yougile_page.last_status_code == 200, f"Ошибка изменения имени. Статус-код: {yougile_page.last_status_code}"

    # 7. Финальная проверка изменения имени
    final_title = yougile_page.get_last_project_title()
    assert final_title == updated_title, f"Имя проекта не обновилось. Ожидали '{updated_title}', в системе: '{final_title}'"

    # 8. Удаление проекта
    yougile_page.delete_project()
