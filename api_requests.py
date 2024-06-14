import requests
import json


#вернут статус на то могут ли они это забронировать
def check_hotel_booking_available():
    r = requests.get(f'http://api:80/get/{id}')
    response = json.loads(r.text)
    return response

#обращаемся чтобы они забронировали
def api_add(id):
    r = requests.post(f'http://api:80/add/{id}')
    response = json.loads(r.text)
    return response

#просим забронировать транспорт какой-то
def transport_book():
    return

#имитация отправки mock запроса
def send_mock_cash():
    r = requests
    return