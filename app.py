from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


# TimeU looks like TimeUntil
class TimeU(BaseModel):
    days: int | None
    hours: int | None
    minutes: int | None
    second: int


class Item(BaseModel):
    id: int
    time_until: TimeU


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cal/")
def read_item(
    jmode: Annotated[
        bool | None,
        Query(title="Calendar mode", description="Hebcal mode's on/off", alias="mode"),
    ] = None,
):
    result = {"message": "Hello world!"}
    if jmode:
        result = {"message": "Shalom Aleihem"}
    return result
