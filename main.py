# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from sum import add_two_numbers

app = FastAPI()

class AddRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
def add_numbers(req: AddRequest):
    result = add_two_numbers(req.a, req.b)
    return {"result": result}
