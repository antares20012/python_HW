from faker import Faker

fake = Faker()
email = fake.email()
subject_id = fake.random_int(5, 15)


class SchoolTable:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    @staticmethod
    def get_last_user(db_cursor):
        db_cursor.execute('SELECT * FROM users ORDER BY user_id DESC LIMIT 1')
        result = db_cursor.fetchone()
        return result

    @staticmethod
    def get_last_added_user_id(db_cursor):
        db_cursor.execute('SELECT * FROM users ORDER BY user_id DESC LIMIT 1')
        result = db_cursor.fetchone()
        last_added_user_id = result[0]
        return last_added_user_id

    @staticmethod
    def get_last_added_user_email(db_cursor):
        db_cursor.execute('SELECT * FROM users ORDER BY user_id DESC LIMIT 1')
        result = db_cursor.fetchone()
        last_added_user_email = result[1]
        return last_added_user_email

    @staticmethod
    def get_last_added_user_subject_id(db_cursor):
        db_cursor.execute('SELECT * FROM users ORDER BY user_id DESC LIMIT 1')
        result = db_cursor.fetchone()
        last_added_user_subject_id = result[2]
        return last_added_user_subject_id

    def insert_new_user(self, db_cursor):
        new_user_id = self.get_last_added_user_id(db_cursor) + 1
        db_cursor.execute("INSERT INTO users (user_id, user_email, subject_id) VALUES (%s, %s, %s)",
                          (new_user_id, email, subject_id))
        db_cursor.execute('SELECT user_id, user_email, subject_id FROM users WHERE user_id = %s', (new_user_id,))
        result = db_cursor.fetchone()
        return result

    def delete_user(self, db_cursor):
        new_user_id = self.get_last_added_user_id(db_cursor) + 1
        db_cursor.execute("INSERT INTO users (user_id, user_email, subject_id) VALUES (%s, %s, %s)",
                          (new_user_id, email, subject_id))
        email_to_be_deleted = self.get_last_added_user_email(db_cursor)
        db_cursor.execute('DELETE FROM users WHERE user_email = %s', (email_to_be_deleted,))
        db_cursor.execute('SELECT from users WHERE user_email = %s', (email_to_be_deleted,))
        result = db_cursor.fetchone()
        return result

    def update_user(self, db_cursor):
        new_user_id = self.get_last_added_user_id(db_cursor) + 1
        db_cursor.execute("INSERT INTO users (user_id, user_email, subject_id) VALUES (%s, %s, %s)",
                          (new_user_id, email, subject_id))
        db_cursor.execute("UPDATE users SET subject_id = %s WHERE user_id = %s", (subject_id, new_user_id))
        db_cursor.execute("SELECT user_id, user_email, subject_id from users WHERE user_id = %s", (new_user_id,))
        result = db_cursor.fetchone()
        return result
