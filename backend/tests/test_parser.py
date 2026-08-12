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
    tokenizer = tokenizer()
    parser = parser()

    ast = parser.parse(tokenizer.tokenize("pi"))

    assert isinstance(ast, ConstantNode)
    assert ast.value == "pi"


def test_parse_function():
    tokenizer = tokenizer()
    parser = parser()

    ast = parser.parse(tokenizer.tokenize("sqrt(9)"))

    assert isinstance(ast, FunctionNode)
    assert ast.name == "sqrt"

    assert isinstance(ast.argument, NumberNode)
    assert ast.argument.value == "9"

