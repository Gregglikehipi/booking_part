from api_requests import send_mock_cash, check_hotel_booking_available, transport_book, book_hotel


def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d


def confirm_hotel(data):
    hotel = without(data, "route_ids")
    hotel_req = check_hotel_booking_available("unknown", hotel)
    hotel_status = 0
    for apartment in hotel_req["apartments"]:
        if not apartment["status"]:
            hotel_status = 1
    if hotel_status == 0:
        book_hotel("unknown", hotel)
    return hotel_req


def confirm_transport(data):
    transports = without(data, "apartments")
    transports = without(transports, "order_id")
    transport_req = transport_book(transports)
    return transport_req


def confirm_all(data):
    hotel = without(data, "route_ids")
    transports = without(data, "apartments")
    transports = without(transports, "order_id")
    hotel_req = check_hotel_booking_available("unknown", hotel)
    hotel_status = 0
    transport_status = 0
    for apartment in hotel_req["apartments"]:
        if not apartment["status"]:
            hotel_status = 1
    transport_req = transport_book(transports)
    for transport in transport_req["route_ids"]:
        if not transport["status"]:
            transport_status = 1
    if transport_status == 0 and hotel_status == 0:
        book_hotel("unknown", hotel)
    data_req = hotel_req.update(transport_req)
    return data_req
