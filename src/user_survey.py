def user_interaction() -> dict | None:
    """ Функция взаимодействия с пользователем для формирования запросов """
    print("Приветствуем! Начнем подбор вакансий в базе данных.")
    counter = 0
    while counter < 3:
        query1 = input("Получаем среднюю зарплату по вакансиям? y/n\n")
        query = input("""Введите 1, 2 или 3 для выбора:
        1 - Получаем все вакансии в базе.
        2 - Получаем вакансии, у которых зарплата выше средней.
        3 - Получаем вакансии по ключевому слову в названии.\n""")
        top_n = input("Введите число, сколько вакансий смотрим:  \n")
        if query == "3":
            user_keyword = input("Введите ключевое слово для поиска: \n")
            # проверяем корректность полученных параметров
            if (is_valid_query1(query1)
                    and is_valid_query(query)
                    and is_valid_top_n(top_n)):
                return {"query1": query1.lower(), "query": query, "keyword": user_keyword, "top_n": top_n}
            else:
                counter += 1
                print("Неверно введены данные для запроса, попробуйте ещё раз")
        else:
            # проверяем корректность полученных параметров
            if (is_valid_query1(query1)
                    and is_valid_query(query)
                    and is_valid_top_n(top_n)):
                return {"query1": query1.lower(), "query": query, "top_n": top_n}
            else:
                counter += 1
                print("Неверно введены данные для запроса, попробуйте ещё раз")


def is_valid_query1(user_words: str) -> bool:
    """ Проверка, что введено y или n"""
    if user_words.lower() in ["y", "n"]:
        return True
    else:
        return False


def is_valid_query(user_word: str) -> bool:
    """проверка, что введено число 1,2 или 3 """
    try:
        if int(user_word) in [1, 2, 3]:
            return True
        else:
            return False
    except ValueError:
        return False


def is_valid_top_n(user_top_n: str) -> bool:
    """проверка, что введено число"""
    try:
        int(user_top_n)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    result = user_interaction()
    print(f"результат: {result}")
