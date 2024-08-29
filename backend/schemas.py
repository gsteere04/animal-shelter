from pydantic import BaseModel


class Animals(BaseModel):
    cats: int
    dogs: int


class Shelter(BaseModel):
    name: str
    id: int
    address: str
    animals: Animals
