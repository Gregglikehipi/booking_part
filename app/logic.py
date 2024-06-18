from app.api_requests import send_mock_cash, check_hotel_booking_available, transport_book, book_hotel

hotel_check = "unknown"
hotel_book = "unknown"
transport_url = "unknown"


def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d


def confirm_hotel(data):
    hotel = without(data, "route_ids")
    hotel_req = check_hotel_booking_available(hotel_check, hotel)
    hotel_status = 0
    for apartment in hotel_req["apartments"]:
        if not apartment["status"]:
            hotel_status = 1
    if hotel_status == 0:
        book_hotel(hotel_book, hotel)
    return hotel_req


def confirm_transport(data):
    transports_req = without(data, "apartments")
    transports = without(transports_req, "order_id")
    transport_req = transport_book(transport_url, transports)
    return transports_req | transport_req


def confirm_all(data):
    hotel = without(data, "route_ids")
    transports = without(data, "apartments")
    transports = without(transports, "order_id")
    hotel_req = check_hotel_booking_available(hotel_check, hotel)
    hotel_status = 0
    transport_status = 0
    for apartment in hotel_req["apartments"]:
        if not apartment["status"]:
            hotel_status = 1
    transport_req = transport_book(transport_url, transports)
    for transport in transport_req["route_ids"]:
        if not transport["status"]:
            transport_status = 1
    if transport_status == 0 and hotel_status == 0:
        book_hotel(hotel_book, hotel)
    return hotel_req | transport_req
