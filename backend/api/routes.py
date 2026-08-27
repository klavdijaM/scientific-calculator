from fastapi import APIRouter
from fastapi import HTTPException

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

    try:
        if request.expression.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Expression cannot be empty."
            )

        tokens = tokenizer.tokenize(request.expression)
        ast = parser.parse(tokens)
        result = evaluator.evaluate(ast)

        return CalculationResponse(result=result)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")