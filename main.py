from datetime import datetime
from typing import Union, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from logic import confirm_all, confirm_transport, confirm_hotel


class Hotel(BaseModel):
    id: int
    start: datetime
    end: datetime


class HotelList(BaseModel):
    list: List[Hotel]


class Transport(BaseModel):
    id: int


class TransportList(BaseModel):
    list: List[Transport]


class HotelReq(Hotel):
    status: bool


class TransportReq(Transport):
    status: bool


class HotelReqList(BaseModel):
    list: List[HotelReq]


class TransportReqList(BaseModel):
    list: List[TransportReq]


class UI(BaseModel):
    user_id: int
    order_id: int
    hotels: Optional[HotelReqList] = []
    transport: Optional[TransportReqList] = []


app = FastAPI()


@app.get("/api/ui_root")
def ui_root(ui: UI):
    data = dict(ui)
    data_req = data
    hotel_bool = False
    transport_bool = False
    if "hotels" in data:
        hotel_bool = True
    if "order_id" in data:
        transport_bool = True
    if hotel_bool and transport_bool:
        data_req = confirm_all(data)
    if not hotel_bool and transport_bool:
        data_req = confirm_transport(data)
    if hotel_bool and not transport_bool:
        data_req = confirm_hotel(data)
    return data_req




