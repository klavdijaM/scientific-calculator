from math import e, pi

from engine.ast import (
    ASTNode, 
    NumberNode, 
    ConstantNode,
    UnaryOperationNode
    )
from engine.token_type import TokenType


class Evaluator:
    """Evaluates an abstract syntax tree."""

    def evaluate(self, node: ASTNode) -> float:
        if isinstance(node, NumberNode):
            return float(node.value)

        elif isinstance(node, ConstantNode):
            if node.value == "pi":
                return pi
            elif node.value == "e":
                return e

        elif isinstance(node, UnaryOperationNode):
            operand = self.evaluate(node.operand)

            if node.operator == TokenType.MINUS:
                return -operand

        raise ValueError(f"Unsupported node type: {type(node).__name__}")
        
