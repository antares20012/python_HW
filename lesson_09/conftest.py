import pytest
import psycopg2


@pytest.fixture(scope="session")
def connection():
    conn = psycopg2.connect(
        dbname="SQL_testing",       # Введите название своей БД
        user="postgres",             # Введите имя пользователя
        password="password",     # Введите свой пароль доступа к БД
        host="localhost",        # Укажите хост базы данных
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
