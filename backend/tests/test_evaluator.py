import math

from engine.token_type import TokenType
from engine.evaluator import Evaluator
from engine.ast import (
    NumberNode, 
    ConstantNode, 
    UnaryOperationNode, 
    BinaryOperationNode,
    FunctionNode
)

def test_evaluate_number():
    evaluator = Evaluator()

    result = evaluator.evaluate(NumberNode("42"))

    assert result == 42.0


def test_evaluate_constant_pi():
    evaluator = Evaluator()
    
    result = evaluator.evaluate(ConstantNode("pi"))
    
    assert result == math.pi


def test_evaluate_constant_e():
    evaluator = Evaluator()

    result = evaluator.evaluate(ConstantNode("e"))

    assert result == math.e


def test_evaluate_unary_minus():
    evaluator = Evaluator()

    node = UnaryOperationNode(
        operator = TokenType.MINUS,
        operand = NumberNode("5")
    )

    assert evaluator.evaluate(node) == -5.0


def test_evaluate_addition():
    evaluator = Evaluator()

    node = BinaryOperationNode(
        operator = TokenType.PLUS,
        left = NumberNode("2"),
        right = NumberNode("3")
    )

    assert evaluator.evaluate(node) == 5.0


def test_evaluate_subtraction():
    evaluator = Evaluator()

    node = BinaryOperationNode(
        operator = TokenType.MINUS,
        left = NumberNode("5"),
        right = NumberNode("3")
    )

    assert evaluator.evaluate(node) == 2.0


def test_evaluate_multiplication():
    evaluator = Evaluator()

    node = BinaryOperationNode(
        operator = TokenType.MULTIPLY,
        left = NumberNode("5"),
        right = NumberNode("3")
    )

    assert evaluator.evaluate(node) == 15.0


def test_evaluate_division():
    evaluator = Evaluator()

    node = BinaryOperationNode(
        operator = TokenType.DIVIDE,
        left = NumberNode("12"),
        right = NumberNode("3")
    )

    assert evaluator.evaluate(node) == 4.0


def test_evaluate_power():
    evaluator = Evaluator()

    node = BinaryOperationNode(
        operator = TokenType.POWER,
        left = NumberNode("4"),
        right = NumberNode("2")
    )

    assert evaluator.evaluate(node) == 16.0


def test_evaluate_func_sqrt():
    evaluator = Evaluator()

    node = FunctionNode(
        name = "sqrt",
        argument = NumberNode("9")
    )

    assert evaluator.evaluate(node) == 3.0


def test_evaluate_func_sin():
    evaluator = Evaluator()

    node = FunctionNode(
        name = "sin",
        argument = NumberNode("0")
    )

    assert evaluator.evaluate(node) == 0.0


def test_evaluate_func_cos():
    evaluator = Evaluator()

    node = FunctionNode(
        name = "cos",
        argument = NumberNode("0")
    )

    assert evaluator.evaluate(node) == 1.0


def test_evaluate_func_log():
    evaluator = Evaluator()

    node = FunctionNode(
        name = "log",
        argument = NumberNode("100")
    )

    assert evaluator.evaluate(node) == 2.0


def test_evaluate_func_ln():
    evaluator = Evaluator()

    node = FunctionNode(
        name = "ln",
        argument = NumberNode(str(math.e))
    )

    assert evaluator.evaluate(node) == 1.0
