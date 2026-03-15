from json_parser.tokens import Token, TokenType


def test_token_creation():
    token = Token(TokenType.STRING, "hello")

    assert token.type == TokenType.STRING
    assert token.value == "hello"