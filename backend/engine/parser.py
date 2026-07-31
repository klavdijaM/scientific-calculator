from engine.token import Token
from engine.token_type import TokenType
from engine.ast import ASTNode, NumberNode, ConstantNode

class Parser:

    """Converts a list of tokens into an abstract syntax tree."""

    def __init__(self):
        self.tokens: list[Token] = []
        self.position = 0
    
    def parse(self, tokens: list[Token]) -> ASTNode:
        self.tokens = tokens 
        self.position = 0

        ast = self._parse_expression()

        if self._current_token().token_type != TokenType.EOF:
            raise ValueError(f"Unexpected token '{self._current_token().value}'")
        
        return ast
    
    def _current_token(self) -> Token:
        return self.tokens[self.position]
    
    def _match(self, expected: TokenType) -> Token:
        token = self._current_token()

        if token.token_type != expected: 
            raise ValueError(f"Expected {expected.name}, got {token.token_type.name} ")
        
        self.position += 1
        return token
    
    def _parse_expression(self) -> ASTNode:
        return self._parse_primary()

    def _parse_primary(self) -> ASTNode:
        token = self._current_token()

        if token.token_type == TokenType.NUMBER:
            self.position += 1
            return NumberNode(token.value)
        
        if token.token_type == TokenType.CONSTANT:
            self.position += 1
            return ConstantNode(token.value)
        
        raise ValueError(f"Unexpected token '{token.value}'")





    

    