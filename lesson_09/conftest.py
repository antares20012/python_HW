import pytest
import psycopg2


@pytest.fixture(scope="session")
def connection():
    conn = psycopg2.connect(
        dbname="my_database",       # Введите название своей БД
        user="my_user",             # Введите имя пользователя
        password="my_password",     # Введите свой пароль доступа к БД
        host="my_localhost",        # Укажите хост базы данных
        port="5432"                 # Укажите порт БД
    )

    with conn.cursor() as cursor:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"\nУспешное подключение! Версия базы: {db_version}")
    yield conn
    conn.close()


@pytest.fixture(scope="session")
def db_cursor(connection):
    cursor = connection.cursor()
    yield cursor
    connection.rollback()
    cursor.close()
