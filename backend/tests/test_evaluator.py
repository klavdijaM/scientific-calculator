import math

from engine.evaluator import Evaluator
from engine.ast import NumberNode, ConstantNode

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

    
