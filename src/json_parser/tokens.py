from enum import Enum, auto


class TokenType(Enum):
    LEFT_BRACE = auto()     # {
    RIGHT_BRACE = auto()    # }
    LEFT_BRACKET = auto()   # [
    RIGHT_BRACKET = auto()  # ]

    COLON = auto()          # :
    COMMA = auto()          # ,

    STRING = auto()         # "hello"
    NUMBER = auto()         # 123, -123, 3.14, -3.14, 1e10, -1e10

    TRUE = auto()           # true
    FALSE = auto()          # false
    NULL = auto()           # null

    EOF = auto()          # End of file/input


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"