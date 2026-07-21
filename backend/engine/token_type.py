from enum import Enum, auto

class TokenType(Enum):

    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    FUNCTION = auto()
    CONSTANT = auto()

    EOF = auto()

    