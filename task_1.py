from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def filtered_list(some_list: list) -> list:
    cursor = 'Россия'
    new_list = []
    for item in some_list:
        for key, value in item.items():
            if cursor in value:
                new_list.append({key: value})
    return new_list

if __name__ == '__main__':
    pprint(filtered_list(geo_logs))
