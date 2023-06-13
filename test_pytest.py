from task_1 import filtered_list
from task_2 import unique_set
from task_4 import find_max_view
import pytest
import requests
from yandex_api import get_headers, create_folder, ya_token, folder_name


class Test_Filtered:

    some_list = [{'visit1': ['Москва', 'Россия']},
                {'visit2': ['Дели', 'Индия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit4': ['Лиссабон', 'Португалия']},
                {'visit5': ['Париж', 'Франция']},
                {'visit6': ['Лиссабон', 'Португалия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}]
    expected_res = [{'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}]

    @pytest.mark.parametrize(
            'some_list, expected_res',
            [(some_list, expected_res),
            ([], [])]
    )
    def test_filtered_list(self, some_list, expected_res):
        res = filtered_list(some_list)
        assert res == expected_res

class Test_Unique:

    some_dict = {'user1': [213, 213, 213, 15, 213],
                'user2': [54, 54, 119, 119, 119],
                'user3': [213, 98, 98, 35]}
    
    expected_res = [213, 15, 54, 119, 98, 35]
    
    @pytest.mark.parametrize(
            'some_dict, expected_res',
            [(some_dict, expected_res)]
    )
    def test_unique_set(self, some_dict, expected_res):
        res = unique_set(some_dict)
        assert res == expected_res


class Test_find_max_view:

    some_stats = {
                'facebook': 55,
                'yandex': 120,
                'vk': 115,
                'google': 99,
                'email': 42,
                'ok': 98
                }
    
    expected_res = 'yandex'
    
    @pytest.mark.parametrize(
            'some_stats, expected_res',
            [(some_stats, expected_res)]
    )
    def test_unique_set(self, some_stats, expected_res):
        res = find_max_view(some_stats)
        assert res == expected_res


class Test_Yandex_API:

    some_folder = folder_name
    
    expected_res = 200
    
    @pytest.mark.parametrize(
            'some_folder, expected_res',
            [(some_folder, expected_res)]
    )
    def test_ya_api(self, some_folder, expected_res):
        href = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = get_headers(ya_token)
        params = {'path': some_folder}
        res = requests.get(f'{href}', headers=headers, params=params).status_code
        assert res == expected_res