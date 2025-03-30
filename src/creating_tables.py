import psycopg2

from config import config


def create_database(database_name: str, params: dict) -> None:
    """ Функция для создания новой базы данных
     и таблиц для данных о работодателях и вакансиях"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")
    finally:
        conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE employers (
                    employer_id integer PRIMARY KEY,
                    name varchar(100),
                    type varchar(50),
                    description text,
                    site_url varchar(100),
                    open_vacancies integer)
                """)
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE vacancies (
                    vacancy_id integer PRIMARY KEY,
                    name varchar(100),
                    salary integer,
                    url varchar(100),
                    schedule varchar(50),
                    created_at varchar(30),
                    employer varchar(100), 
                    employer_id integer REFERENCES employers(employer_id))
                """)
    finally:
        conn.close()


if __name__ == "__main__":
    params = config()
    print(params)

    create_database("hh_vacancies", params)
