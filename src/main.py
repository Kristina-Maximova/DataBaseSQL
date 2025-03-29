from src.api_guide import get_employer_data, get_vacancies
from src.config import config
from src.creating_tables import create_database
from src.db_manager import DBManager
from src.save_data_to_tables import save_employers_data, save_vacancies_data
from src.user_survey import user_interaction
from src.vacancy import Vacancy

database_name = "hh_vacancies"
my_employers_ids = ["10122709", "9917029", "2398387",
                    "584898", "11075933", "6113620",
                    "2866992", "864086", "2853703",
                    "1687807", "10634659", "11679140",
                    "4716984", "3571722"]


def main() -> None:
    """ Функция для объединения всех операций и получения вывода"""
    # Получение данных с сайта hh.ru
    emp1_list = []
    for elem in my_employers_ids:
        emp1_list.append(get_employer_data(elem))  # список по работодателям
    vacs_list = []
    for elem in my_employers_ids:
        vacs_list += get_vacancies(elem)  # список по вакансиям каждого работодателя

    params = config()
    # Создание BD и заполнение таблиц:
    create_database("hh_vacancies", params)
    save_employers_data(emp1_list, database_name, params)
    save_vacancies_data(vacs_list, database_name, params)

    # Получение пользовательских настроек
    user_settings = user_interaction()  # {'query1': 'y', 'query': '3', 'keyword': 'Python', 'top_n': '3'}

    # Выполнение запросов
    db_manager0 = DBManager(database_name, params)
    if user_settings['query1'] == 'y':
        query3 = db_manager0.get_avg_salary()
        print(f"Cредняя зарплата: {query3["avg"]} руб.")

    user_vacancies = []
    db_manager1 = DBManager(database_name, params)
    if user_settings['query'] == "1":
        user_vacancies += db_manager1.get_all_vacancies()
    elif user_settings['query'] == "2":
        user_vacancies += db_manager1.get_vacancies_with_higher_salary()
    elif user_settings['query'] == "3":
        user_vacancies += db_manager1.get_vacancies_with_keyword(user_settings['keyword'])

    # Формирование вывода
    vacancies_list = Vacancy.cast_to_object_list(user_vacancies)
    print(f"Сейчас вакансий в списке: {len(vacancies_list)}")
    if vacancies_list:
        if len(vacancies_list) >= int(user_settings['top_n']):
            for vac in vacancies_list[0:int(user_settings['top_n'])]:
                print(vac)
        elif len(vacancies_list) < int(user_settings['top_n']):
            for vac in range(len(vacancies_list)):
                print(vac)
    else:
        print("Не найдено вакансий по заданным условиям")


if __name__ == "__main__":
    main()

    # Выполнение запросов
    # db_manager1 = DBManager(database_name, params)
    # query1 = db_manager1.get_companies_and_vacancies_count()
    # for elem in query1:
    #     print(f"Компания {elem['employer']}, вакансий: {elem['vacancies_count']}")
