from pprint import pprint

stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
    }

def find_max_view(some_dict: dict) -> str:
    most_viewed = sorted(some_dict.items(), key=lambda item: item[1])[-1][0]
    return most_viewed


if __name__ == '__main__':
    pprint(find_max_view(stats))