from pydantic import BaseModel

class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float