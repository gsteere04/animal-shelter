from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import Animals, Shelter

shelters: list[Shelter] = [
    Shelter(
        id=1,
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animals(
            cats=13,
            dogs=15,
        ),
    ),
    Shelter(
        id=2,
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animals(
            cats=12,
            dogs=9,
        ),
    ),
    Shelter(
        id=3,
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animals(
            cats=4,
            dogs=7,
        ),
    ),
    Shelter(
        id=4,
        name="Bailey's Rescued Animals",
        address="25 Main St, St. George, UT 84770",
        animals=Animals(
            cats=0,
            dogs=0,
        ),
    ),
    Shelter(
        id=5,
        name="Izzy's Home for Cute Cats",
        address="28 Main St, St. George, UT 84770",
        animals=Animals(
            cats=10,
            dogs=0,
        ),
    ),
]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/shelters")
async def get_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters")
async def add_shelter(new_shelter: Shelter) -> list[Shelter]:
    for shelter in shelters:
        if shelter.name == new_shelter.name:
            raise HTTPException(status_code=400, detail="Shelter already exists.")
    
    shelters.append(new_shelter)
    return shelters

@app.put("/shelters")
async def update_shelter(updated_shelter: Shelter) -> list[Shelter]:
    for index, shelter in enumerate(shelters):
        if shelter.id == updated_shelter.id:
            shelters[index] = updated_shelter
            return shelters
    
    shelters.append(updated_shelter)
    return shelters

@app.delete("/shelters")
async def delete_shelter(deleted_shelter: Shelter):
    for index, shelter in enumerate(shelters):
        if shelter.id == deleted_shelter.id:
            del shelters[index]
            return {"detail": "Shelter deleted successfully."}
    
    raise HTTPException(status_code=404, detail="Shelter not found.")
