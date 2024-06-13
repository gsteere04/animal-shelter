from pydantic import BaseModel


class Animals(BaseModel):
    cats: int
    dogs: int


class Shelter(BaseModel):
    name: str
    address: str
    animals: Animals
