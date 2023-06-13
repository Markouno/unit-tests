from pprint import pprint

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_set(some_dict: dict) -> list:
    new_unique_list = []
    for key, value in some_dict.items():
        for item in value:
            if item not in new_unique_list:
                new_unique_list.append(item)
    return new_unique_list


if __name__ == '__main__':
    pprint(unique_set(ids))