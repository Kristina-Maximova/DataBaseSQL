from typing import Any

from config import config
import psycopg2


def save_employers_data(data: list[dict[str, Any]],
                        database_name: str,
                        params: dict):
    """ Функция для сохранения данных о работодателях в таблицу базы данных"""
    conn = psycopg2.connect(dbname=database_name, **params)
    try:
        with conn:
            with conn.cursor() as cur:
                for employer in data:
                    cur.execute(
                        """
                        INSERT INTO employers (employer_id, name,
                         type, description, site_url, open_vacancies)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (employer['employer_id'],
                         employer['name'],
                         employer['type'],
                         employer['description'],
                         employer['site_url'],
                         employer['open_vacancies'],)
                    )
    finally:
        conn.close()


def save_vacancies_data(data: list[dict[str, Any]],
                        database_name: str,
                        params: dict):
    """ Функция для сохранения данных о вакансиях в таблицу базы данных """
    conn = psycopg2.connect(dbname=database_name, **params)
    try:
        with conn:
            with conn.cursor() as cur:
                for vacancy in data:
                    cur.execute(
                        """
                        INSERT INTO vacancies (vacancy_id, name, salary, 
                        url, schedule, created_at, employer, employer_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (vacancy['vacancy_id'],
                         vacancy['name'],
                         vacancy['salary'],
                         vacancy['url'],
                         vacancy['schedule'],
                         vacancy['created_at'],
                         vacancy['employer'],
                         vacancy['employer_id'])
                    )
    finally:
        conn.close()


if __name__ == "__main__":
    database_name = "hh_vacancies"
