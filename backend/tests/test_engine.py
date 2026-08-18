import math

from engine.tokenizer import Tokenizer
from engine.parser import Parser
from engine.evaluator import Evaluator

def evaluate(expression: str) -> float:
    tokenizer = Tokenizer()
    parser = Parser()
    evaluator = Evaluator()

    tokens = tokenizer.tokenize(expression)
    ast = parser.parse(tokens)
    float = evaluator.evaluate(ast)

    return float


def test_integer():
    assert evaluate("42") == 42.0


def test_decimal():
    assert evaluate("42.5") == 42.5


def test_addition():
    assert evaluate("2+3") == 5.0


def test_subtraction():
    assert evaluate("5-2") == 3.0


def test_multiplication():
    assert evaluate("4*3") == 12.0


def test_division():
    assert evaluate("8/2") == 4.0


def test_power():
    assert evaluate("2^3") == 8.0


def test_operator_precedence():
    assert evaluate("2+3*4") == 14.0


def test_parentheses():
    assert evaluate("(2+3)*4") == 20.0


def test_nested_expression():
    assert evaluate("2+(4-2)^2") == 6.0


def test_unary_minus():
    assert evaluate("-5") == -5.0


def test_constant():
    assert evaluate("pi") == math.pi


def test_sqrt():
    assert evaluate("sqrt(9)") == 3.0


def test_log():
    assert evaluate("log(100)") == 2.0


def test_ln():
    assert evaluate(f"ln({math.e})") == 1.0