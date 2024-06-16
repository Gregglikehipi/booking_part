from datetime import datetime
from typing import Union, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from logic import confirm_all


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
    status: str


class TransportReq(Transport):
    status: str


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
    data_req = confirm_all(data)
    return data_req




