from engine.token import Token
from engine.token_type import TokenType

class Tokenizer:

    def __init__(self):
        self.expression = ""
        self.position = 0

    def tokenize(self, expression: str) -> list[Token]:
        self.expression = expression 
        self.position = 0
        tokens: list[Token] = []

        while self.position < len(self.expression):
            current_char = self.expression[self.position]

            if current_char.isspace():
                self.position += 1

            elif current_char == "+":
                tokens.append(Token(TokenType.PLUS, "+"))
                self.position += 1

            elif current_char == "-":
                tokens.append(Token(TokenType.MINUS, "-"))
                self.position += 1

            elif current_char == "*":
                tokens.append(Token(TokenType.MULTIPLY, "*"))
                self.position += 1

            elif current_char == "/":
                tokens.append(Token(TokenType.DIVIDE, "/"))
                self.position += 1

            elif current_char == "^":
                tokens.append(Token(TokenType.POWER, "^"))
                self.position += 1

            elif current_char == "(":
                tokens.append(Token(TokenType.LEFT_PAREN, "("))
                self.position += 1

            elif current_char == ")":
                tokens.append(Token(TokenType.RIGHT_PAREN, ")"))
                self.position += 1
            
            else:
                raise ValueError(f"Unexpected character '{current_char}' at position {self.position}")

        tokens.append(Token(TokenType.EOF, ""))

        return tokens

