import typer
import sys

from json_parser.lexer import Lexer
from json_parser.parser import Parser

app = typer.Typer()


def validate_json(text: str):
    lexer = Lexer(text)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    parser.parse()


@app.command()
def validate(file: str = None):

    try:

        if file:
            with open(file) as f:
                text = f.read()
        else:
            text = sys.stdin.read()

        validate_json(text)

        print("Valid JSON")

    except Exception:
        print("Invalid JSON")
        raise typer.Exit(code=1)


@app.command()
def version():
    print("json-parser v1.0")


if __name__ == "__main__":
    app()