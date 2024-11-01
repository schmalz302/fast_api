
from models import *
from fastapi import Depends
from sqlalchemy.orm import Session
from db import db


#

def get_all_user_crud():
	with db as session:
		users = session.query(User_db).all()
		return {"message": f"Пользователи - {users}"}

def create_users_crud():
	with db as session:
		user1 = User_db(name="Egor", age=20)
		user2 = User_db(name="Lef", age=19)
		user3 = User_db(name="Ivan", age=22)
		user4 = User_db(name="Petr", age=33)
		user5 = User_db(name="Slava", age=56)
		session.add_all([user1, user2, user3, user4, user5])
		session.commit()
		users = session.query(User_db).all()
		return {"message": f"Пользователи - {users} успешно созданы"}

def delete_users_crud():
	with db as session:
		users = session.query(User_db).all()
		for i in users:
			session.delete(i)
		session.commit()
		return {"message": f"Пользователи - успешно удалены"}


def get_user_crud(id: int):
	with db as session:
		user = session.get(User_db, id)
		if user:
			return {"message": f"Пользователь - {user}"}
		return {"message": f"Пользователя с id = {id} не существует"}
#
def create_user_crud(user: User_db):
	with db as session:
		session.add(user)
		session.commit()
		session.refresh(user)
		return {"message": f"Пользователь {user} - создан"}

def delete_user_crud(id: int):
	with db as session:
		user = session.get(User_db, id)
		if user:
			session.delete(user)
			session.commit()
			return {"message": f"Пользователь - {user} - успешно удален"}
		else:
			return {"message": f"Пользователя с id = {id} не существует"}

def change_user_crud(new_user: User_db):
	with db as session:
		current_user = session.get(User_db, new_user.id)
		if current_user:
			current_user.name = new_user.name
			current_user.age = new_user.age
			session.commit()
			session.refresh()
			return {"message": f"Пользователь - {new_user} - успешно обновлен"}
		else:
			return {"message": f"Пользователя с id = {new_user.id} не существует"}




def get_all_cars_crud():
	with db as session:
		cars = session.query(Car_db).all()
		return {"message": f" - Автомобили {cars}"}


def create_cars_crud():
	with db as session:
		car1 = Car_db(brand="Lada", price=120, configuration="Standart")
		car2 = Car_db(brand="Opel", price=100, configuration="Comfort")
		car3 = Car_db(brand="Skoda", price=300, configuration="Basic equipment")
		car4 = Car_db(brand="Skoda", price=111, configuration="Luxury")
		car5 = Car_db(brand="Toyota", price=156, configuration="Basic equipment")
		car6 = Car_db(brand="Honda", price=144, configuration="Comfort")
		car7 = Car_db(brand="Suzuki", price=99, configuration="Basic equipment")
		session.add_all([car1, car2, car3, car4, car5, car6, car7])
		session.commit()
		cars = session.query(Car_db).all()
		return {"message": f"Автомобили - {cars} успешно созданы"}

def delete_cars_crud():
	with db as session:
		cars = session.query(Car_db).all()
		for i in cars:
			session.delete(i)
		session.commit()
		return {"message": f"Автомобили - успешно удалены"}




def get_car_crud(id: int):
	with db as session:
		car = session.get(Car_db, id)
		if car:
			return {"message": f"Автомобиль - {car}"}
		return {"message": f"Автомобиля с id = {id} не существует"}
#
def create_car_crud(car: Car_db):
	with db as session:
		session.add(car)
		session.commit()
		session.refresh(car)
		return {"message": f"Автомобиль {car} - создан"}

def delete_car_crud(id: int):
	with db as session:
		car = session.get(Car_db, id)
		if car:
			session.delete(car)
			session.commit()
			return {"message": f"Автомобиль - {car} - успешно удален"}
		else:
			return {"message": f"Автомобиля с id = {id} не существует"}

def change_car_crud(new_car: Car_db):
	with db as session:
		current_car = session.get(Car_db, new_car.id)
		if current_car:
			current_car.brand = new_car.brand
			current_car.price = new_car.price
			current_car.configuration = new_car.configuration
			session.commit()
			session.refresh()
			return {"message": f"Автомобиль - {new_car} - успешно обновлен"}
		else:
			return {"message": f"Автомобиля с id = {new_car.id} не существует"}


def get_all_orders_crud():
	with db as session:
		orders = session.query(Order_db).all()
		return {"message": f" - Заказы {orders}"}

def create_orders_crud():
	pass

