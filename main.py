# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sum import add_two_numbers  # your custom module

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class AddRequest(BaseModel):
    a: float
    b: float

# POST endpoint
@app.post("/add")
def add_numbers(req: AddRequest):
    result = add_two_numbers(req.a, req.b)
    print("hi")
    return {"result": result}
