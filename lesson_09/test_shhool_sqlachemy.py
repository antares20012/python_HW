from SchoolTableSqlalchemy import SchoolTableSqlalchemy

db = SchoolTableSqlalchemy("postgresql://postgres:password@localhost:5432/SQL_testing")

def test_get_users():
    db_result = db.get_users()
    assert len(db_result) > 0
    assert db_result is not None

def test_get_last_added_user():
    db_result = db.get_last_added_user()
    assert db_result is not None
    assert db_result['user_id'] is not None
    assert db_result['user_email'] is not None
    assert db_result['subject_id'] is not None


def test_insert_user():
    last_user_before = db.get_last_added_user()
    expected_new_id = int(last_user_before["user_id"]) + 1
    db_result = db.insert_user()
    assert db_result is not None
    new_user = db.get_last_added_user()
    db.delete_user_by_id(expected_new_id)
    assert new_user['user_id'] == expected_new_id
    assert "@" in new_user['user_email']
    assert  1<=new_user['subject_id']<=15

def test_delete_user_by_id():
    before = len(db.get_users())
    db.insert_user()
    db.delete_user_by_id(id)
    after = len(db.get_users())
    assert after - before == 0

def test_update_last_added_user():
    db.insert_user()
    subject_before = db.get_last_added_user()['subject_id']
    db.update_last_added_user(id)
    subject_after = db.get_last_added_user()['subject_id']
    db.delete_user_by_id(id)
    assert subject_after != subject_before










