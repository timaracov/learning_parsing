from pprint import pprint as pp

from src.tokenizer import Tokenizer
from src.parser import Parser


if __name__ == "__main__":
    from sys import argv

    tokens = []
    with open(argv[1]) as f:
        data = f.read()

    print("---")
    print(data)
    print("---")

    p = Parser(Tokenizer(data))
    p.parse()

    pp(p._exprs)
