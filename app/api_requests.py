import requests
import json

data_all = {
    "user_id": 4,
    "order_id": 1,
    "apartments": [
        {
            "id": 1,
            "start": '2032-04-23T10:20:30.400+02:30',
            "end": '2032-04-23T10:20:30.400+02:30',
            "status": True
        },
        {
            "id": 2,
            "start": '2032-04-23T10:20:30.400+02:30',
            "end": '2032-04-23T10:20:30.400+02:30',
            "status": True
        }
    ],
    "route_ids": [
        {
            "id": 1,
            "status": False
        },
        {
            "id": 2,
            "status": True
        }
    ]
}

start_data = {
    "user_id": 4,
    "order_id": 1,
    "apartments": [
        {
            "id": 1,
            "start": '2032-04-23',
            "end": '2032-04-23'
        },
        {
            "id": 2,
            "start": '2032-04-23',
            "end": '2032-04-23'
        }
    ],
    "route_ids": [
        1,
        2,
        3
    ]
}

data_hotel = {
    "user_id": 0,
    "order_id": 0,
    "apartments": [
        {
            "id": 0,
            "status": True
        },
    ]
}

data_true = {
  "user_id": 0,
  "order_id": 0,
  "apartments": [
    {
      "id": 0,
      "start": "2024-06-17T17:49:47.244Z",
      "end": "2024-06-17T17:49:47.244Z"
    }
  ],
  "route_ids": [
    1,
    2,
    3
  ]
}

data_transport = {
    "success": False,
    "failed_ids": [
        1,
        3
    ],
    "message": "ошибка бронирования некоторых рейсов"
}


#вернут статус на то могут ли они это забронировать
def check_hotel_booking_available(address, data):
    if address == "unknown":
        return data_hotel
    response = requests.post(address, json=data)
    return json.loads(response.text)


#обращаемся чтобы они забронировали
def book_hotel(address, data):
    if address == "unknown":
        print("hi")
    else:
        requests.post(address, json=data)


#просим забронировать транспорт какой-то
def transport_book(address, data):
    # сюда положим элементы изначального списка
    routes = {"route_ids": []}
    for i in data["route_ids"]:
        routes["route_ids"].append({"id": i, "status": True})
    js_dict = []
    if address == "unknown":
        js_dict = data_transport
    else:
        response = requests.post(address, json=data)
        js_dict = json.loads(response.text)
    #ответ апи
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
