from dataclasses import dataclass
from engine.token_type import TokenType

@dataclass
class Token:
    token_type: TokenType
    value: str