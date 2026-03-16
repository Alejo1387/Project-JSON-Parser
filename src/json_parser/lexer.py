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

            elif char == '"':
                tokens.append(self.read_string())
                continue

            self.position += 1

        tokens.append(Token(TokenType.EOF))
        return tokens

    def read_string(self):
        self.position += 1
        start = self.position

        while self.position < len(self.text) and self.text[self.position] != '"':
            self.position += 1

        value = self.text[start:self.position]

        self.position += 1

        return Token(TokenType.STRING, value)