from pydantic import BaseModel

class TrainSchema(BaseModel):
    first_row: str
    second_row: str

class People(BaseModel):
    name: str
    surname: str
    age: int

