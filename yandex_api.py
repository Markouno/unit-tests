import requests
import pytest

ya_token = 'y0_AgAAAAAXdNOfAADLWwAAAADdiYIZW6qKJJ-XTxSkfttvj9HcOFpMB-Y'
folder_name = 'test-case'


def get_headers(ya_token):
    return {'Content-Type': 'applictaion/json',
            'Authorization': 'OAuth {}'.format(ya_token)}


def create_folder(folder_name: str):
    href = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = get_headers(ya_token)
    params = {'path': folder_name}
    response = requests.put(f'{href}', headers=headers, params=params)
    return response.status_code

print(create_folder(folder_name))



    
    

