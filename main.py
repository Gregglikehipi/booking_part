from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI


class Hotel(BaseModel):
    nm_id: int
    name: str
    name: str
    brand: str
    brand_id: int
    site_brand_id: int


class Transport(BaseModel):
    nm_id: int
    name: str
    name: str
    brand: str
    brand_id: int
    site_brand_id: int


class HotelReq(BaseModel):
    nm_id: int
    name: str
    name: str
    brand: str
    brand_id: int
    site_brand_id: int


class TransportReq(BaseModel):
    nm_id: int
    name: str
    name: str
    brand: str
    brand_id: int
    site_brand_id: int


app = FastAPI()


@app.get("/ui_root")
def ui_root(hotel: Hotel, transport: Transport):
    return {"Name": hotel.name}


@app.get("/transport_root")
def transport_root():
    return {"Hello": "World"}


@app.get("/hotel_root")
def hotel_root():
    return {"Hello": "World"}


