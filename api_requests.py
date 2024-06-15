import requests

#вернут статус на то могут ли они это забронировать
def check_hotel_booking_available(address, data):
    response = requests.post("unknown", json=data)
    return response.text

#обращаемся чтобы они забронировали
def book_hotel(address, data):
    response = requests.post("unknown", json=data)
    return response.text

#просим забронировать транспорт какой-то
def transport_book(data):
    response = requests.post("http://api/v1/book", json=data)
    return response.text

#имитация отправки mock запроса
def send_mock_cash():
    response = requests.get("https://mock.httpstatus.io/202")
    return response.status_code

