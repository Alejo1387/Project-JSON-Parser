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
                
            elif char.isdigit() or char == "-":
                tokens.append(self.read_number())
                continue

            elif char.isalpha():
                tokens.append(self.read_keyword())
                continue


            self.position += 1

        tokens.append(Token(TokenType.EOF))
        return tokens

    def read_string(self):
        self.position += 1
        start = self.position

        while self.position < len(self.text) and self.text[self.position] != '"':
            self.position += 1

        if self.position >= len(self.text):
            raise ValueError("Unterminated string")

        value = self.text[start:self.position]

        self.position += 1

        return Token(TokenType.STRING, value)
    
    def read_number(self):
        start = self.position

        while self.position < len(self.text) and (
            self.text[self.position].isdigit()
            or self.text[self.position] in ".eE+-"
        ):
            self.position += 1

        num_str = self.text[start:self.position]

        if "." in num_str or "e" in num_str or "E" in num_str:
            value = float(num_str)
        else:
            value = int(num_str)

        return Token(TokenType.NUMBER, value)

    def read_keyword(self):
        start = self.position

        while self.position < len(self.text) and self.text[self.position].isalpha():
            self.position += 1

        word = self.text[start:self.position]

        if word == "true":
            return Token(TokenType.TRUE, True)

        elif word == "false":
            return Token(TokenType.FALSE, False)

        elif word == "null":
            return Token(TokenType.NULL, None)

        else:
            raise ValueError(f"Unexpected keyword: {word}")
