from pydantic import BaseModel


class Animal(BaseModel):
    animal_type: str
    count: int = 0


class Shelter(BaseModel):
    name: str
    address: str
    animals: list[Animal]
