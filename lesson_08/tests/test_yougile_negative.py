from pages.yougile_page_negative import YougileApi


def test_yougile_negative(credentials):

    yougile_page_negative = YougileApi("https://ru.yougile.com/api-v2", credentials=credentials)
    company_id = yougile_page_negative.get_yougile_my_company_id()
    print(f"ID Вашей компании {company_id}")
    assert company_id is not None, "Не удалось получить ID компании"
    assert yougile_page_negative.last_status_code == 200, f"Ожидали статус 200, получили {yougile_page_negative.last_status_code}"

    token = yougile_page_negative.create_yougile_my_key()
    print(f"Ваш токен API {token}")
    assert token is not None, "API-ключ не был сгенерирован"
    assert yougile_page_negative.last_status_code in [200,201], f"Неверный статус-код при создании ключа: {yougile_page_negative.last_status_code}"

    fetched_key = yougile_page_negative.get_yougile_my_key()
    print(fetched_key)
    assert fetched_key is not None, "Не удалось запросить текущие API-ключи"
    assert yougile_page_negative.last_status_code == 201, f"Ожидали статус 201 при запросе ключа, получили {yougile_page_negative.last_status_code}"

    target_title = "QA Automation Project"
    project_data = yougile_page_negative.create_project_negative(title=target_title)
    assert yougile_page_negative.last_status_code in [401], "Негативная проверка не удалась, в запросе вы передали все данные"
    assert isinstance(project_data, dict), f"Ожидался словарь (JSON объект), получен {type(project_data)}"
    assert project_data.get("message") == "Unauthorized", f"Проект был создан id ({project_data.get("id")})"

    yougile_page_negative.create_project_positive(title=target_title)
    yougile_page_negative.get_last_project_title_negative()
    current_title = yougile_page_negative.get_last_project_title_negative()
    assert current_title is None

    updated_title = "QA Automation Project - Updated"
    update_res = yougile_page_negative.update_project_negative(new_title=updated_title)
    assert update_res is not None, "Сервер вернул пустой ответ при обновлении проекта"
    assert yougile_page_negative.last_status_code == 401

    yougile_page_negative.delete_project()
