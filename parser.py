from tokenizer import Token

class Parser:
    def __init__(self, tokens: list[Token]):
        self._tokens = tokens
        self._expressions = []
        self._stack = []
        self._current_expresssion = None
