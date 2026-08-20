from fastapi import APIRouter

from api.schemas import CalculationRequest, CalculationResponse
from engine.parser import Parser
from engine.tokenizer import Tokenizer
from engine.evaluator import Evaluator 

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello from fastAPI"}

@router.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest) -> CalculationResponse:

    tokenizer = Tokenizer()
    parser = Parser()
    evaluator = Evaluator()

    tokens = tokenizer.tokenize(request.expression)
    ast = parser.parse(tokens)
    result = evaluator.evaluate(ast)

    return CalculationResponse(result=result)