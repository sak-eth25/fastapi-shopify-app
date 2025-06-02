from fastapi import FastAPI
from pydantic import BaseModel
from sum import add_two_numbers

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/sum")
def calculate_sum(numbers: Numbers):
    result = add_two_numbers(numbers.a, numbers.b)
    return {"sum": result}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
