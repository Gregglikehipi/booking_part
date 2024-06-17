from datetime import datetime
from typing import Union, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from app.logic import confirm_all, confirm_transport, confirm_hotel


class Hotel(BaseModel):
    id: int
    start: datetime
    end: datetime


class UI(BaseModel):
    user_id: int
    order_id: int
    apartments: List[Hotel] = []
    route_ids: List[int] = []


app = FastAPI()


@app.post("/api/ui_root")
def ui_root(ui: UI):
    data = dict(ui)
    data_req = data
    hotel_bool = False
    transport_bool = False
    if data["apartments"]:
        hotel_bool = True
    if data["route_ids"]:
        transport_bool = True
    if hotel_bool and transport_bool:
        data_req = confirm_all(data)

    if not hotel_bool and transport_bool:
        data_req = confirm_transport(data)
    if hotel_bool and not transport_bool:
        data_req = confirm_hotel(data)
    return data_req




