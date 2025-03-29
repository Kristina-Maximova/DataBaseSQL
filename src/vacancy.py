from src.api_guide import get_vacancies


class Vacancy:
    """ Класс для представления вакансии"""
    __slots__ = ("vacancy_id", "name", "salary", "created_at", "url", "schedule", "employer", "employer_id")

    def __init__(self, vacancy_id: int, name: str, salary: float | None,
                 url: str, schedule: str, created_at: str | None, employer: str, employer_id: int) -> None:
        """ Конструктор класса вакансия для создания объектов"""
        self.vacancy_id = vacancy_id
        self.name = name
        self.salary = salary if salary else 0.0
        self.url = url
        self.schedule = schedule
        self.created_at = created_at
        self.employer = employer
        self.employer_id = employer_id

    def __str__(self) -> str:
        """ Метод строкового отображения вакансии """
        return f"Компания: {self.employer}, вакансия: {self.name}, зарплата: {self.salary} руб., {self.url}"

    @classmethod
    def cast_to_object_list(cls, data_with_vacancies: list[dict | None]) -> list:
        """ Класс-метод для преобразования списка словарей в список объектов класса"""
        if len(data_with_vacancies) == 0:
            return []
        else:
            new_vacancies_obj = []
            try:
                for vacancy in data_with_vacancies:
                    vacancy_obj = cls(**vacancy)
                    new_vacancies_obj.append(vacancy_obj)
                return new_vacancies_obj
            except AttributeError:
                print("Ошибка преобразования данных в объект класса Vacancy")
                return []

    @property
    def to_dict(self) -> dict | None:  # с декоратором вызов без круглых скобок
        return {"vacancy_id": self.vacancy_id,
                "name": self.name,
                "salary": self.salary,
                "url": self.url,
                "schedule": self.schedule,
                "created_at": self.created_at,
                "employer": self.employer,
                "employer_id": self.employer_id}

if __name__=="__main__":
    my_employers_id = ["10122709", "9917029", "2398387",
                       "584898", "11075933", "6113620",
                       "2866992", "864086", "2853703",
                       "1687807", "10634659", "11679140",
                       "4716984", "3571722"]
    # получение списка словарей с данными о вакансиях
    vac_1_a = get_vacancies("2853703")
    # Создание объектов Vacancy из данных
    user_vacancies = Vacancy.cast_to_object_list(vac_1_a)
    print(f"Сейчас в списке выбрано вакансий: {len(user_vacancies)}")
    for vac in user_vacancies[0:3]:
        print(vac)
