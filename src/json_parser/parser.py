from json_parser.tokens import TokenType


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position]

    def eat(self, token_type):
        token = self.current_token()

        if token.type == token_type:
            self.position += 1
            return token
        else:
            raise ValueError(f"Expected {token_type}, got {token.type}")

    def parse(self):
        return self.parse_value()