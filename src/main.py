from src.config import config
from src.api_guide import get_employer_data, get_vacancies
from src.creating_tables import create_database







if __name__ == "__main__":
    my_employers_id = ["10122709", "9917029", "2398387",
                       "584898", "11075933", "6113620",
                       "2866992", "864086", "2853703",
                       "1687807", "10634659", "11679140",
                       "4716984", "3571722"]
    emp1 = get_employer_data("10122709")
    # print(emp1)
    vac1 = get_vacancies("2853703")
    # for vac in vac1:
    #     print(vac)
    params = config()
    print(params)
    create_database("hh_vacancies", params)
