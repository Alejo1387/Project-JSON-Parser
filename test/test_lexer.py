import pytest
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

def test_string_token():
    lexer = Lexer('"hello"')
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.STRING
    assert tokens[0].value == "hello"
    assert tokens[1].type == TokenType.EOF

def test_object_with_string():
    lexer = Lexer('{"name":"alex"}')
    tokens = lexer.tokenize()

    assert tokens[0].type.name == "LEFT_BRACE"
    assert tokens[1].value == "name"
    assert tokens[3].value == "alex"

def test_unterminated_string():
    lexer = Lexer('"hello')

    with pytest.raises(ValueError):
        lexer.tokenize()

def test_integer_number():
    lexer = Lexer("123")
    tokens = lexer.tokenize()

    assert tokens[0].value == 123

def test_float_number():
    lexer = Lexer("3.14")
    tokens = lexer.tokenize()

    assert tokens[0].value == 3.14

def test_negative_number():
    lexer = Lexer("-5")
    tokens = lexer.tokenize()

    assert tokens[0].value == -5

def test_true_token():
    lexer = Lexer("true")
    tokens = lexer.tokenize()

    assert tokens[0].value is True

def test_false_token():
    lexer = Lexer("false")
    tokens = lexer.tokenize()

    assert tokens[0].value is False

def test_null_token():
    lexer = Lexer("null")
    tokens = lexer.tokenize()

    assert tokens[0].value is None