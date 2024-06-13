from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import Animals, Shelter

# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a `list[Shelter]`. You don't need to write code to convert
# this list, just manually change it by hand.
shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animals(
            cats=13,
            dogs=15,
        ),
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animals(
            cats=12,
            dogs=9,
        ),
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animals(
            cats=4,
            dogs=7,
        ),
    ),
    Shelter(
        name="Bailey's Rescued Animals",
        address="25 Main St, St. George, UT 84770",
        animals=Animals(
            cats=0,
            dogs=0,
        ),
    ),
    Shelter(
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
