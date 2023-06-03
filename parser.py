from pprint import pprint

from typing import Type
from tokenizer import (
    Token, TokenType, Tokenizer,
    SYMBOLS, KEYWORDS, SCOPES, TYPES
)


BIN_EXP = {
    (SYMBOLS["<"], SYMBOLS["="]): "lt",
    (SYMBOLS[">"], SYMBOLS["="]): "gt",
    (SYMBOLS["!"], SYMBOLS["="]): "ne",
    (SYMBOLS["+"], SYMBOLS["="]): "pe",
    (SYMBOLS["/"], SYMBOLS["="]): "de",
    (SYMBOLS["-"], SYMBOLS["="]): "me",
    (SYMBOLS["*"], SYMBOLS["="]): "mue",
    (SYMBOLS["="], SYMBOLS["="]): "eq",
    (SYMBOLS["-"], SYMBOLS[">"]): "rt",
}

TYPE_DEF = [
    (KEYWORDS["var"], scope,SYMBOLS[":"], type_,SYMBOLS[":"])
    for scope in SCOPES.values()
    for type_ in TYPES.values()
]

pprint(TYPE_DEF)


class Parser:
    def __init__(self, tokenizer: Tokenizer):
        self._tokenizer: Tokenizer = tokenizer
        self._cur_token = None
        self._stack = []
        self._exprs = []
        self._sub_parsers = (
            self._parse_bin_expr,
            self._parse_type_def_expr,
        )

        self.next_token_and_push_stack()

    def next_token_and_push_stack(self):
        self._cur_token = self._tokenizer.next_token()
        self._stack.append(self._cur_token)

    def parse(self):
        while self._cur_token.token_type != TokenType.EOF: # type:ignore
            for parser_func in self._sub_parsers:
                parser_func()

    def _parse_bin_expr(self):
        self.next_token_and_push_stack()
        pair = self._stack[-2], self._stack[-1]
        if pair in BIN_EXP:
            self._exprs.append((BIN_EXP[pair], pair))
            self._stack = []

    def _parse_type_def_expr(self):
        self.next_token_and_push_stack()
        if tuple(self._stack) in TYPE_DEF:
            self.next_token_and_push_stack()
            if self._cur_token.token_type == TokenType.NAME:  # type:ignore
                self._exprs.append(("type_def", *self._stack))
                self._stack = []

