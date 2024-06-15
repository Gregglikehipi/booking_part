from api_requests import send_mock_cash


def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d


def confirm(data):
    data = {
        "user_id": 4,
        "order_id": 1,
        "apartments": [
           {
               "id": 1,
               "start": 21,
               "end": 23
           },
           {
               "id": 2,
               "start": 26,
               "end": 29,
           }
        ],
        "route_ids": [
            1,
            2,
            3
        ]
    }
    hotel = without(data, "route_ids")
    transports = without(data, "apartments")
    hotel_req = {}  # TODO: Add send_mock_cash()
    hotel_status = 0
    transport_status = 0
    for apartment in hotel["apartments"]:  # TODO: Change hotel to hotelReq
        if apartment["status"] == "No":
            hotel_status = 1
    transport_req = {}  # TODO: Add send_mock_cash()
    for transport in transports["route_ids"]:  # TODO: Change transports to transportReq
        if transport["status"] == "No":
            transport_status = 1
    if transport_status == 0 and hotel_status == 0:
        send_mock_cash()  # TODO: Put hotel
    hotel_req.update(transport_req)
    data_req = {
        "user_id": 4,
        "order_id": 1,
        "apartments": [
            {
                "id": 1,
                "start": 21,
                "end": 23,
                "status": "No"
            },
            {
                "id": 2,
                "start": 26,
                "end": 29,
                "status": "No"
            }
        ],
        "route_ids": [
            {
                "id": 1,
                "status": "No"
            },
            {
                "id": 2,
                "status": "No"
            },
            {
                "id": 3,
                "status": "No"
            }
        ]
    }
    return data_req
