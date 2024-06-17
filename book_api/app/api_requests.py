import requests
import json


#вернут статус на то могут ли они это забронировать
def check_hotel_booking_available(address, data):
    response = requests.post("unknown", json=data)
    return json.loads(response.text)


#обращаемся чтобы они забронировали
def book_hotel(address, data):
    response = requests.post("unknown", json=data)
    return json.loads(response.text)


#просим забронировать транспорт какой-то
def transport_book(data):
    # сюда положим элементы изначального списка
    routes = {"route_ids": []}
    print(data)
    for i in data["route_ids"]:
        routes["route_ids"].append({"id": i, "status": True})

    #стучимся в апи
    response = requests.post("http://api/v1/book", json=data)
    #ответ апи
    js_dict = json.loads(response.text)
    if len(js_dict["failed_ids"]) == 0:
        return routes
    else:
        for i in js_dict["failed_ids"]:
            for j in routes["route_ids"]:
                if j["id"] == i:
                    j["status"] = False
        return routes




#имитация отправки mock запроса
def send_mock_cash():
    response = requests.get("https://mock.httpstatus.io/202")
    return response.status_code


