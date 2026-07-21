from fastapi import APIRouter
from api.schemas import CalculationRequest

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello from fastAPI"}

@router.post("/calculate")
def calculate(request: CalculationRequest):
    return {"expression": request.expression}