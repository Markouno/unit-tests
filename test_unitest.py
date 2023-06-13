from unittest import TestCase
from task_1 import filtered_list, geo_logs
from task_2 import unique_set, ids
from task_4 import find_max_view, stats
import requests
from yandex_api import get_headers, ya_token, folder_name



class FilteredTestCase(TestCase):
    def test_filter_case(self):
        data_ = geo_logs
        expected_res = [{'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}]

        res = filtered_list(data_)
        self.assertEqual(res, expected_res)


class UniqueTesting(TestCase):
    def test_unique_list(self):
        data_ = ids
        expected_res = [213, 15, 54, 119, 98, 35]
        res = unique_set(data_)
        self.assertEqual(res, expected_res)


class FindMaxTesting(TestCase):
    def test_find_max(self):
        data_ = stats
        expected_res = 'yandex'
        res = find_max_view(data_)
        self.assertEqual(res, expected_res)


class CheckFolderYandex(TestCase):
    def test_checking_folder(self):
        expected_res = 200
        href = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = get_headers(ya_token)
        params = {'path': folder_name}
        res = requests.get(f'{href}', headers=headers, params=params).status_code
        self.assertEqual(res, expected_res)