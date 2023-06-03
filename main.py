from pprint import pprint as pp

from tokenizer import Tokenizer, TokenType
from parser import Parser


if __name__ == "__main__":
    from sys import argv

    with open(argv[1]) as f:
        data = f.read()
    print("---")
    print(data)
    print("---")

    tokens = []
    p = Parser(Tokenizer(data))
    p.parse()
    pp(p._exprs)
