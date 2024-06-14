import requests
import json


def api_get(id):
    r = requests.get(f'http://api:80/get/{id}')
    response = json.loads(r.text)
    return response


def api_add(id):
    r = requests.post(f'http://api:80/add/{id}')
    response = json.loads(r.text)
    return response