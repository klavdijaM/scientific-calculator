from math import e, pi

from engine.ast import (
    ASTNode, 
    NumberNode, 
    ConstantNode,
    UnaryOperationNode,
    BinaryOperationNode,
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

        elif isinstance(node, BinaryOperationNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.operator == TokenType.PLUS:
                return left + right

            elif node.operator == TokenType.MINUS:
                return left - right

            elif node.operator == TokenType.MULTIPLY:
                return left * right

            elif node.operator == TokenType.DIVIDE:
                return left / right

            elif node.operator == TokenType.POWER:
                return left ** right

        raise ValueError(f"Unsupported node type: {type(node).__name__}")
        
