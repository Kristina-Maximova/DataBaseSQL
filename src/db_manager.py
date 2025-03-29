import psycopg2


class DBManager:
    """ Класс для работы с таблицами в базе данных postgres"""

    def __init__(self, database_name: str, params: dict, ):
        """ Конструктор класса для работы с таблицами в базе данных postgres """
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> list[dict] | None:
        """ Метод для получения списка всех компаний
         и количества вакансий у каждой компании"""
        try:
            with self.conn:
                self.cur = self.conn.cursor()
                with self.cur as cur:
                    cur.execute("""
                    SELECT DISTINCT e.name, COUNT(v.*) as vacancies_count
                    FROM employers e
                    FULL JOIN vacancies v USING(employer_id)
                    GROUP BY e.employer_id
                    ORDER BY vacancies_count DESC;
                    """)
                    data = self.cur.fetchall()
                    data_in_dict = [{"employer": d[0], "vacancies_count": d[1]} for d in data]
                    return data_in_dict
        finally:
            self.conn.close()

    def get_all_vacancies(self) -> list[dict] | None:
        """ Метод для получения списка всех вакансий """
        try:
            with self.conn:
                self.cur = self.conn.cursor()
                with self.cur as cur:
                    cur.execute("""
                    SELECT v.*
                    FROM vacancies v
                    FULL JOIN employers e USING(employer_id);
                    """)
                    data = self.cur.fetchall()
                    vacancies_in_dict = [{"vacancy_id": d[0],
                                          "name": d[1],
                                          "salary": d[2],
                                          "url": d[3],
                                          "schedule": d[4],
                                          "created_at": d[5],
                                          "employer": d[6],
                                          "employer_id": d[7]}
                                         for d in data]
                    return vacancies_in_dict
        finally:
            self.conn.close()

    def get_avg_salary(self) -> dict | None:
        """ Метод для получения средней зарплаты по вакансиям"""
        try:
            with self.conn:
                self.cur = self.conn.cursor()
                with self.cur as cur:
                    cur.execute("""
                    SELECT AVG(v.salary)::real as average_salary
                    FROM vacancies v 
                    WHERE v.salary IS NOT NULL;
                    """)
                    data = self.cur.fetchall()
                    return {"avg": data[0][0]}
        finally:
            self.conn.close()

    def get_vacancies_with_higher_salary(self) -> list[dict] | None:
        """ Метод для получения списка вакансий,
        у которых зарплата выше среднего значения по всем вакансиям"""
        try:
            with self.conn:
                self.cur = self.conn.cursor()
                with self.cur as cur:
                    cur.execute("""
                    SELECT v.*
                    FROM vacancies v
                    WHERE  v.salary > (SELECT AVG(v.salary)::real FROM vacancies v 
                    WHERE v.salary IS NOT NULL)
                    ORDER BY v.salary DESC;
                    """)
                    data = self.cur.fetchall()
                    vacancies_in_dict = [{"vacancy_id": d[0],
                                          "name": d[1],
                                          "salary": d[2],
                                          "url": d[3],
                                          "schedule": d[4],
                                          "created_at": d[5],
                                          "employer": d[6],
                                          "employer_id": d[7]}
                                         for d in data]
                    return vacancies_in_dict
        finally:
            self.conn.close()

    def get_vacancies_with_keyword(self, keyword: str) -> list[dict] | None:
        """ Метод для получения вакансий
        по ключевому слову в названии """
        try:
            with self.conn:
                self.cur = self.conn.cursor()
                with self.cur as cur:
                    cur.execute(f"""
                    SELECT v.*
                    FROM vacancies v
                    WHERE v.name LIKE '%{keyword}%';
                    """)
                    data = self.cur.fetchall()
                    vacancies_in_dict = [{"vacancy_id": d[0],
                                          "name": d[1],
                                          "salary": d[2],
                                          "url": d[3],
                                          "schedule": d[4],
                                          "created_at": d[5],
                                          "employer": d[6],
                                          "employer_id": d[7]}
                                         for d in data]
                    return vacancies_in_dict
        finally:
            self.conn.close()
