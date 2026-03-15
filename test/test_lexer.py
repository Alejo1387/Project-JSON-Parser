from json_parser.lexer import Lexer
from json_parser.tokens import TokenType


def test_simple_object_tokens():
    lexer = Lexer("{}")
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.LEFT_BRACE
    assert tokens[1].type == TokenType.RIGHT_BRACE
    assert tokens[2].type == TokenType.EOF

def test_array_tokens():
    lexer = Lexer("[]")
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.LEFT_BRACKET
    assert tokens[1].type == TokenType.RIGHT_BRACKET
    assert tokens[2].type == TokenType.EOF

def test_whitespace_ignored():
    lexer = Lexer("{   }")
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.LEFT_BRACE
    assert tokens[1].type == TokenType.RIGHT_BRACE
    assert tokens[2].type == TokenType.EOF
