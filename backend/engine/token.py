from dataclasses import dataclass
from engine.token_type import TokenType

@dataclass
class Token:
    type: TokenType
    value: str