from dataclasses import dataclass
from engine.token_type import TokenType

class ASTNode:
    """Base class for all AST nodes."""
    pass

@dataclass 
class NumberNode(ASTNode):
    value: str

@dataclass
class ConstantNode(ASTNode):
    value: str

@dataclass
class UnaryOperationNode(ASTNode):
    operator: TokenType
    operand: ASTNode

@dataclass
class BinaryOperationNode(ASTNode):
    operator: TokenType
    left: ASTNode
    right: ASTNode

@dataclass 
class FunctionNode(ASTNode):
    name: str
    argument: ASTNode

