from sqlalchemy import create_engine, text
from faker import Faker

fake = Faker()



class SchoolTableSqlalchemy:

    connection_string = "postgresql://postgres:password@localhost:5432/SQL_testing"

    __scripts = {
        "select users": text("select * from users"),
        "select last added user": text("SELECT * FROM users ORDER BY user_id DESC LIMIT 1"),
        "insert user": text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id)"),
        "delete user by id": text("DELETE FROM users WHERE user_id = :user_id"),
        "update user last added user": text("UPDATE users SET subject_id = :subject_id WHERE user_id = :user_id")

    }

    def __init__(self, connection_string):
        # conn = connection_string
        self.__db = create_engine(connection_string)

    def get_users(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select users"])
            rows = result.mappings().all()
            return rows

    def get_last_added_user(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select last added user"])
            rows = result.mappings().all()
            if not rows:
                return None
            return rows[0]

    def insert_user(self):
        with self.__db.connect() as conn:
            last_user_id = int(self.get_last_added_user()["user_id"])
            new_user_id = last_user_id + 1
            user_email = fake.email()
            subject_id = fake.random_int(1, 15)


            result = conn.execute(
                self.__scripts["insert user"],
                {"user_id": new_user_id, "user_email": user_email, "subject_id": subject_id}
            )
            conn.commit()
            return result

    def delete_user_by_id(self, id):
        with self.__db.connect() as conn:
            last_user_id = int(self.get_last_added_user()["user_id"])
            result = conn.execute(self.__scripts["delete user by id"],
                                  {"user_id": last_user_id}
            )
            conn.commit()
            return result

    def update_last_added_user(self, id):
        with self.__db.connect() as conn:
            last_user_id = int(self.get_last_added_user()["user_id"])
            subject_id = fake.random_int(1, 15)
            result = conn.execute(self.__scripts["update user last added user"],
                                  {"user_id": last_user_id, "subject_id": subject_id})
            conn.commit()
            new_subject_id = int(self.get_last_added_user()["subject_id"])
            return new_subject_id

