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
        value = self.parse_value()

        if self.current_token().type != TokenType.EOF:
            raise ValueError("Unexpected data after JSON value")

        return value
    
    def parse_value(self):
        token = self.current_token()

        if token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return token.value

        elif token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return token.value

        elif token.type == TokenType.TRUE:
            self.eat(TokenType.TRUE)
            return True

        elif token.type == TokenType.FALSE:
            self.eat(TokenType.FALSE)
            return False

        elif token.type == TokenType.NULL:
            self.eat(TokenType.NULL)
            return None

        elif token.type == TokenType.LEFT_BRACE:
            return self.parse_object()

        elif token.type == TokenType.LEFT_BRACKET:
            return self.parse_array()

        else:
            raise ValueError(f"Unexpected token: {token.type}")
    
    def parse_object(self):
        obj = {}

        self.eat(TokenType.LEFT_BRACE)

        if self.current_token().type == TokenType.RIGHT_BRACE:
            self.eat(TokenType.RIGHT_BRACE)
            return obj

        while True:
            key_token = self.eat(TokenType.STRING)
            key = key_token.value

            self.eat(TokenType.COLON)

            value = self.parse_value()

            obj[key] = value

            if self.current_token().type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
            else:
                break

        self.eat(TokenType.RIGHT_BRACE)

        return obj
    
    def parse_array(self):
        array = []

        self.eat(TokenType.LEFT_BRACKET)

        if self.current_token().type == TokenType.RIGHT_BRACKET:
            self.eat(TokenType.RIGHT_BRACKET)
            return array

        while True:
            value = self.parse_value()
            array.append(value)

            if self.current_token().type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
            else:
                break

        self.eat(TokenType.RIGHT_BRACKET)

        return array