from json_parser.tokens import Token, TokenType


class Lexer:

    def __init__(self, text):
        self.text = text
        self.position = 0

    def tokenize(self):
        tokens = []

        while self.position < len(self.text):
            char = self.text[self.position]

            if char.isspace():
                self.position += 1
                continue

            if char == "{":
                tokens.append(Token(TokenType.LEFT_BRACE))

            elif char == "}":
                tokens.append(Token(TokenType.RIGHT_BRACE))

            elif char == "[":
                tokens.append(Token(TokenType.LEFT_BRACKET))

            elif char == "]":
                tokens.append(Token(TokenType.RIGHT_BRACKET))

            elif char == ":":
                tokens.append(Token(TokenType.COLON))

            elif char == ",":
                tokens.append(Token(TokenType.COMMA))

            self.position += 1

        tokens.append(Token(TokenType.EOF))
        return tokens
