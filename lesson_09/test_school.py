from SchoolTable import SchoolTable


def test_insert_new_user(db_cursor):
    table = SchoolTable(db_cursor)
    result = table.insert_new_user(db_cursor)
    expected_user_id = table.get_last_added_user_id(db_cursor)
    expected_user_email = table.get_last_added_user_email(db_cursor)
    expected_user_subject_id = table.get_last_added_user_subject_id(db_cursor)
    assert result[0] == expected_user_id
    assert result[1] == expected_user_email
    assert result[2] == expected_user_subject_id


def test_update_user(db_cursor):
    table = SchoolTable(db_cursor)
    result = table.update_user(db_cursor)
    expected_user_id = table.get_last_added_user_id(db_cursor)
    expected_user_email = table.get_last_added_user_email(db_cursor)
    expected_user_subject_id = table.get_last_added_user_subject_id(db_cursor)
    assert result[0] == expected_user_id
    assert result[1] == expected_user_email
    assert result[2] == expected_user_subject_id


def test_delete_user(db_cursor):
    table = SchoolTable(db_cursor)
    result = table.delete_user(db_cursor)
    assert result is None
