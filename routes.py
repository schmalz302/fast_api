from fastapi import APIRouter, Body
from random import randint as r

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from schemes import TrainSchema, People
from crud import *
api_router = APIRouter()

@api_router.get('/get_all_user')
def get_all_user():
    return get_all_user_crud()

@api_router.post('/create_users')
def create_users():
    return create_users_crud()

@api_router.delete('/delete_users')
def delete_users():
    return delete_users_crud()

# http://127.0.0.1:8000/get_user?id=1
@api_router.get('/get_user')
def get_user(id: int):
    return get_user_crud(id)


@api_router.post('/create_user')
def create_user(data=Body()):
    name = data["name"]
    age = data["age"]
    user = User_db(name=name, age=age)
    return create_user_crud(user)


@api_router.delete('/delete_user')
def delete_user(id: int):
    return delete_user_crud(id)

@api_router.put('/change_user')
def change_user(data=Body()):
    id = data["id"]
    name = data["name"]
    age = data["age"]
    user = User_db(id=id, name=name, age=age)
    return change_user_crud(user)



@api_router.get('/get_all_cars')
def get_all_cars():
    return get_all_cars_crud()

@api_router.post('/create_cars')
def create_cars():
    return create_cars_crud()

@api_router.delete('/delete_cars')
def delete_cars():
    return delete_cars_crud()


@api_router.get('/get_car')
def get_car(id: int):
    return get_car_crud(id)


@api_router.post('/create_car')
def create_car(data=Body()):
    brand = data["brand"]
    price = data["price"]
    configuration = data["configuration"]
    car = Car_db(brand=brand, price=price, configuration=configuration)
    return create_car_crud(car)


@api_router.delete('/delete_car')
def delete_car(id: int):
    return delete_car_crud(id)

@api_router.put('/change_car')
def change_car(data=Body()):
    brand = data["brand"]
    price = data["price"]
    configuration = data["configuration"]
    car = Car_db(brand=brand, price=price, configuration=configuration)
    return change_car_crud(car)


@api_router.get('/get_all_orders')
def get_all_orders():
    return get_all_orders_crud()

@api_router.post('/create_orders')
def create_orders():
    return create_orders_crud()

