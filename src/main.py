from src.config import config
from src.api_guide import get_employer_data, get_vacancies
from src.creating_tables import create_database
from src.save_data_to_tables import (save_employers_data,
                                     save_vacancies_data)
from src.db_manager import DBManager





if __name__ == "__main__":
    database_name = "hh_vacancies"
    my_employers_ids = ["10122709", "9917029", "2398387",
                       "584898", "11075933", "6113620",
                       "2866992", "864086", "2853703",
                       "1687807", "10634659", "11679140",
                       "4716984", "3571722"]
    emp1 = get_employer_data("10122709")
    emp1_list = []
    for elem in my_employers_ids:
        emp1_list.append(get_employer_data(elem)) # список по работодателям

    vacs_list = []
    for elem in my_employers_ids:
        vacs_list += get_vacancies(elem) # список по вакансиям каждого работодателя

    params = config()
    # Создание BD и заполнение таблиц:
    create_database("hh_vacancies", params)
    save_employers_data(emp1_list, database_name, params)
    save_vacancies_data(vacs_list,database_name, params)

    # Выполнение запросов
    db_manager1 = DBManager(database_name, params)
    # query1 = db_manager1.get_companies_and_vacancies_count()
    # for elem in query1:
    #     print(f"Компания {elem['employer']}, вакансий: {elem['vacancies_count']}")

    # query2 = db_manager1.get_all_vacancies()
    # print(query2[0:3])

    # query3 = db_manager1.get_avg_salary()
    # print(f"Cредняя зарплата: {query3["avg"]} руб.")

    # query4 = db_manager1.get_vacancies_with_higher_salary()
    # for vac in query4[0:3]:
    #     print(vac)

    query5 = db_manager1.get_vacancies_with_keyword("Python")
    for vac in query5[0:3]:
        print(vac)
