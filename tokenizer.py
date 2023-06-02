from enum import Enum
from pprint import pprint as pp


alph = "qwertyuiopasdfghjklzxcvbnm"
alph += alph.upper()


class Token(Enum):
    BRACKET_SQRL_L = "{"
    BRACKET_SQRL_R = "}"
    BRACKET_SQR_L  = "["
    BRACKET_SQR_R  = "["
    BRACKET_L      = "("
    BRACKET_R      = ")"
    QUOT_SINGLE    = "'"
    QUOT_DOUBLE    = '"'
    SEMICOL        = ";"
    PLUS           = "+"
    MULT           = "*"
    MINUS          = "-"
    ASSIGN         = "="
    COMA           = ','
    DOT            = "."
    EOF            = "\0"
    KWRD_VAR       = "var"
    KWRD_RET       = "ret"
    KWRD_USE       = "use"
    KWRD_DEF       = "define"
    ILLEGAL        = lambda val: ("ILL", val)
    NAME           = lambda val: ("ident", val)
    NUMBER         = lambda val: ("decimal", val)


SYMBOLS = {
    "{": Token.BRACKET_SQRL_L ,
    "}": Token.BRACKET_SQRL_R ,
    "[": Token.BRACKET_SQR_L,
    "[": Token.BRACKET_SQR_R,  
    "(": Token.BRACKET_L,  
    ")": Token.BRACKET_R,
    "'": Token.QUOT_SINGLE,
    '"': Token.QUOT_DOUBLE,
    ";": Token.SEMICOL,
    "+": Token.PLUS,
    "*": Token.MULT,
    "-": Token.MINUS,
    "=": Token.ASSIGN,
    ",": Token.COMA,         
    ".": Token.DOT,
}


KEYWORDS = {
    "var"   : Token.KWRD_VAR,
    "ret"   : Token.KWRD_RET, 
    "use"   : Token.KWRD_USE, 
    "define": Token.KWRD_DEF, 
}


class Tokenizer:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.position = 0
        self.char = self.input_string[self.position]

    def next_token(self):
        if self.position >= len(self.input_string):
            return Token.EOF

        self.char = self.input_string[self.position]
        match self.char:
            case "{": 
                self.position += 1
                return Token.BRACKET_SQRL_L
            case "}":
                self.position += 1
                return Token.BRACKET_SQRL_R
            case "[":
                self.position += 1
                return Token.BRACKET_SQR_L
            case "[":
                self.position += 1
                return Token.BRACKET_SQR_R
            case "(":
                self.position += 1
                return Token.BRACKET_L
            case ")":
                self.position += 1
                return Token.BRACKET_R
            case "'":
                self.position += 1
                return Token.QUOT_SINGLE
            case '"':
                self.position += 1
                return Token.QUOT_DOUBLE
            case ";":
                self.position += 1
                return Token.SEMICOL
            case "+":
                self.position += 1
                return Token.PLUS
            case "*":
                self.position += 1
                return Token.MULT
            case "-":
                self.position += 1
                return Token.MINUS
            case "=":
                self.position += 1
                return Token.ASSIGN
            case ',':
                self.position += 1
                return Token.COMA
            case ".":
                self.position += 1
                return Token.DOT
            case _:
                if self.is_whitespace(self.char):
                    self.position += 1
                    return self.next_token()
                elif self.is_letter(self.char):
                    return self.build_word()
                elif self.is_number(self.char):
                    return self.build_number()
                else:
                    self.position += 1
                    return Token.ILLEGAL(self.char) # type:ignore

    def build_word(self):
        word = ""
        while self.is_letter(self.char):
            word += self.char
            self.position += 1
            if self.position >= len(self.input_string):
                break
            self.char = self.input_string[self.position]

        if word in KEYWORDS:
            return KEYWORDS[word]
        return Token.NAME(word) # type:ignore

    def build_number(self):
        num = ""
        while self.is_number(self.char):
            num += self.char
            self.position += 1
            if self.position >= len(self.input_string):
                break
            self.char = self.input_string[self.position]
        return Token.NUMBER(num) # type:ignore

    def is_whitespace(self, char):
        return char in [" ", "\t", "\r", "\n"]

    def is_letter(self, char):
        return char in alph+"_"

    def is_number(self, char):
        return char in (str(n) for n in range(10))




inp = \
"""\
use 'package';


var a, b = 123, 2;

var int:define_value;

define func(a=0, b=2) {
    var c = ?a*b-1;
    ret c;
}

define main() {
    func(a, b);
}
"""


if __name__ == "__main__":
    tokens = []
    tokenizer = Tokenizer(inp)
    while (token := tokenizer.next_token()) != Token.EOF:
        tokens.append(token)
    pp(tokens)
