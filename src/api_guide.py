import requests


def get_employer_data(employer_id: str) -> dict | None:
    """ Функция для получения с сайта HH данных о работодателе
     по id работодателя"""
    url = f"https://api.hh.ru/employers/{employer_id}"
    params = {
        "HH-User-Agent": "User-Agent",
    }
    try:
        response = requests.get(url, params=params)
        status_code = response.status_code
        data = response.json()

        if data:
            result = {
                'employer_id': data.get('id'),
                'name': data.get('name'),
                'type': data.get('type'),
                'description': data.get('description'),
                'site_url': data.get('site_url'),
                'open_vacancies': data.get('open_vacancies')
            }
            return result
        else:
            return {'employer_id': f"{employer_id}"}
    except Exception as e:
        print(f'Ошибка получения данных о работодателе {e}, статус код {status_code}')


def get_vacancies(employer_id: str) -> list | None:
    """ Функция для получения данных о вакансиях конкретного работодателя """
    url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'
    params = {
        'area': 1,
        'only_with_salary': True
    }
    try:
        response = requests.get(url, params=params)
        status_code = response.status_code
        data = response.json()
        vacancies = data['items']  # список словарей с данными

        result = []
        for vacancy in vacancies:
            vacancy_data = {
                'vacancy_id': vacancy.get('id'),
                'name': vacancy.get('name'),
                'salary': vacancy.get('salary', {}).get('from', 0.0),
                'url': vacancy.get('url'),
                'schedule': vacancy.get('schedule', {}).get('name'),
                'created_at': vacancy.get('created_at'),
                'employer': vacancy.get('employer', {}).get('name'),
                'employer_id': vacancy.get('employer', {}).get('id')
            }
            result.append(vacancy_data)
        return result
    except Exception as e:
        print(f'Ошибка получения данных о вакансиях: {e}, статус код {status_code}')


if __name__ == "__main__":
    my_employers_id = ["10122709", "9917029", "2398387",
                       "584898", "11075933", "6113620",
                       "2866992", "864086", "2853703",
                       "1687807", "10634659", "11679140",
                       "4716984", "3571722"]

    emp_1_a = get_employer_data("2853703")
    print(emp_1_a)

    vac_1_a = get_vacancies("2853703")
    print(vac_1_a)
