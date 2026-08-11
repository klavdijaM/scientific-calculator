import pytest
from engine.tokenizer import Tokenizer
from engine.token_type import TokenType

def test_tokenize_integer():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("42")

    assert len(tokens) == 2
    assert tokens[0].token_type == TokenType.NUMBER
    assert tokens[0].value == "42"
    assert tokens[1].token_type == TokenType.EOF


def test_tokenize_decimal():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("3.14")

    assert len(tokens) == 2
    assert tokens[0].token_type == TokenType.NUMBER
    assert tokens[0].value == "3.14"
    assert tokens[1].token_type == TokenType.EOF


def test_tokenize_all_operators():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("+-*/^")

    assert len(tokens) == 6 
    
    assert tokens[0].token_type == TokenType.PLUS
    assert tokens[0].value == "+"

    assert tokens[1].token_type == TokenType.MINUS
    assert tokens[1].value == "-"

    assert tokens[2].token_type == TokenType.MULTIPLY
    assert tokens[2].value == "*"

    assert tokens[3].token_type == TokenType.DIVIDE
    assert tokens[3].value == "/"

    assert tokens[4].token_type == TokenType.POWER
    assert tokens[4].value == "^"

    assert tokens[5].token_type == TokenType.EOF
    assert tokens[5].value == ""


def test_tokenize_parentheses():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("()")

    assert len(tokens) == 3

    assert tokens[0].token_type == TokenType.LEFT_PAREN
    assert tokens[0].value == "("

    assert tokens[1].token_type == TokenType.RIGHT_PAREN
    assert tokens[1].value == ")"

    assert tokens[2].token_type == TokenType.EOF


def test_tokenize_constant():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("pi")

    assert len(tokens) == 2

    assert tokens[0].token_type == TokenType.CONSTANT
    assert tokens[0].value == "pi"

    assert tokens[1].token_type == TokenType.EOF


def test_tokenize_function():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("sin")

    assert len(tokens) == 2

    assert tokens[0].token_type == TokenType.FUNCTION
    assert tokens[0].value == "sin"

    assert tokens[1].token_type == TokenType.EOF


def test_tokenize_expression():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("3+2")

    assert len(tokens) == 4

    assert tokens[0].token_type == TokenType.NUMBER
    assert tokens[0].value == "3"

    assert tokens[1].token_type == TokenType.PLUS
    assert tokens[1].value == "+"

    assert tokens[2].token_type == TokenType.NUMBER
    assert tokens[2].value == "2"

    assert tokens[3].token_type == TokenType.EOF


def test_tokenize_whitespace():
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("  2 + 3  ")

    assert len(tokens) == 4

    assert tokens[0].token_type == TokenType.NUMBER
    assert tokens[0].value == "2"

    assert tokens[1].token_type == TokenType.PLUS
    assert tokens[1].value == "+"

    assert tokens[2].token_type == TokenType.NUMBER
    assert tokens[2].value == "3"

    assert tokens[3].token_type == TokenType.EOF


def test_unknown_identifier():
    tokenizer = Tokenizer()

    with pytest.raises(ValueError):
        tokenizer.tokenize("abc")


def test_unexpected_character():
    tokenizer = Tokenizer()

    with pytest.raises(ValueError):
        tokenizer.tokenize("@")


    









