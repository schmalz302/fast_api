from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class User_db(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())
    age: Mapped[int] = mapped_column(Integer())
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))

    def __repr__(self) -> str:
        return f"User_db(id={self.id}, name={self.name}, age={self.age})"


class Order_db(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped["User_db"] = relationship(
        "User_db")
    car: Mapped["Car_db"] = relationship(
        "Car_db")

    def __repr__(self) -> str:
        return f"Order_db(id={self.id}, users={str(self.user)}, cars={str(self.car)})"




class Car_db(Base):
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column(Integer())
    configuration: Mapped[str] = mapped_column(String())
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))

    def __repr__(self) -> str:
        return (f"Car_db(id={self.id}, brand={self.brand}, price={self.price}, configuration: "
                f"{self.configuration})")



