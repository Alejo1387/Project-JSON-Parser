from json_parser.lexer import Lexer
from json_parser.parser import Parser


def test_parse_number():
    lexer = Lexer("123")
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    result = parser.parse()

    assert result == 123

def test_parse_simple_object():
    lexer = Lexer('{"a":1}')
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    result = parser.parse()

    assert result == {"a": 1}

def test_parse_array():
    lexer = Lexer("[1,2,3]")
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    result = parser.parse()

    assert result == [1,2,3]

def test_extra_data_after_json():
    lexer = Lexer('{"a":1} true')
    tokens = lexer.tokenize()

    parser = Parser(tokens)

    import pytest
    with pytest.raises(ValueError):
        parser.parse()