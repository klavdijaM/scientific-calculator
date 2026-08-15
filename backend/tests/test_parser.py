import pytest
from engine.parser import Parser
from engine.tokenizer import Tokenizer
from engine.token_type import TokenType
from engine.ast import (
    NumberNode,
    ConstantNode,
    UnaryOperationNode,
    BinaryOperationNode,
    FunctionNode

)

def test_parse_number():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("42"))

    assert isinstance(ast, NumberNode)
    assert ast.value == "42"


def test_parse_constant():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("pi"))

    assert isinstance(ast, ConstantNode)
    assert ast.value == "pi"


def test_parse_function():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("sqrt(9)"))

    assert isinstance(ast, FunctionNode)
    assert ast.name == "sqrt"

    assert isinstance(ast.argument, NumberNode)
    assert ast.argument.value == "9"


def test_unary_minus():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("-5"))

    assert isinstance(ast, UnaryOperationNode)
    assert ast.operator == TokenType.MINUS

    assert isinstance(ast.operand, NumberNode)
    assert ast.operand.value == "5"


def test_parse_addition():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("2+3"))

    assert isinstance(ast, BinaryOperationNode)
    assert ast.operator == TokenType.PLUS

    assert isinstance(ast.left, NumberNode)
    assert ast.left.value == "2"

    assert isinstance(ast.right, NumberNode)
    assert ast.right.value == "3"


def test_parse_operator_precedence():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("2+3*4"))

    assert isinstance(ast, BinaryOperationNode)
    assert ast.operator == TokenType.PLUS

    assert isinstance(ast.left, NumberNode)
    assert ast.left.value == "2"

    assert isinstance(ast.right, BinaryOperationNode)
    assert ast.right.operator == TokenType.MULTIPLY

    assert ast.right.left.value == "3"
    assert ast.right.right.value == "4"


def test_parse_parentheses():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("(2+3)*4"))

    assert isinstance(ast, BinaryOperationNode)
    assert ast.operator == TokenType.MULTIPLY

    assert isinstance(ast.left, BinaryOperationNode)
    assert ast.left.operator == TokenType.PLUS

    assert ast.left.left.value == "2"
    assert ast.left.right.value == "3"

    assert isinstance(ast.right, NumberNode)
    assert ast.right.value == "4"


def test_parse_power():
    tokenizer = Tokenizer()
    parser = Parser()

    ast = parser.parse(tokenizer.tokenize("2^2^3"))

    assert isinstance(ast, BinaryOperationNode)
    assert ast.operator == TokenType.POWER

    assert ast.left.value == "2"

    assert isinstance(ast.right, BinaryOperationNode)
    assert ast.right.operator == TokenType.POWER

    assert ast.right.left.value == "2"
    assert ast.right.right.value == "3"


def test_invalid_expression():
    tokenizer = Tokenizer()
    parser = Parser()

    with pytest.raises(ValueError):
        parser.parse(tokenizer.tokenize("2+"))


def test_unexpected_token():
    tokenizer = Tokenizer()
    parser = Parser()

    with pytest.raises(ValueError):
        parser.parse(tokenizer.tokenize(")"))














    
    

    