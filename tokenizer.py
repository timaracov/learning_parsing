import typing as t

from enum import Enum


alph = "qwertyuiopasdfghjklzxcvbnm"
alph += alph.upper()


class TokenType(Enum):
    BRACKET_SQRL_L  = "{"
    BRACKET_SQRL_R  = "}"
    BRACKET_SQR_L   = "["
    BRACKET_SQR_R   = "]"
    BRACKET_L       = "("
    BRACKET_R       = ")"
    QUOT_SINGLE     = "'"
    QUOT_DOUBLE     = '"'
    SEMICOL         = ";"
    COLON           = ":"
    GT              = ">"
    LT              = "<"
    PLUS            = "+"
    MULT            = "*"
    MINUS           = "-"
    ASSIGN          = "="
    AAT             = "@"
    SLASH           = "/"
    BSLASH          = "\\"
    HASHT           = "#"
    EXMARK          = "!"
    QMARK           = "?"
    AMPER           = "&"
    COMA            = ','
    DOT             = "."
#    NEWLINE         = "\n"
    # special
    EOF             = "\0"
    ILLEGAL         = "illegal"
    NAME            = "name"
    NUMBER          = "number"
    INDENT          = "indent"
    # types : expressions???
    TYPE_INT8       = "int8"
    TYPE_INT16      = "int16"
    TYPE_INT32      = "int32"
    TYPE_UINT8      = "uint8"
    TYPE_UINT16     = "uint16"
    TYPE_UINT32     = "uint32"
    TYPE_FLOAT32    = "float32"
    TYPE_FLOAT64    = "float64"
    TYPE_BOOL       = "bool"
    TYPE_STRING     = "string"
    TYPE_NULL       = "null"
    TYPE_CALLABLE   = "call"
    # keywords
    KWRD_TRY        = "try"
    KWRD_VAR        = "var"
    KWRD_RET        = "ret"
    KWRD_USE        = "use"
    KWRD_FUNC       = "func"
    KWRD_STRUCT     = "struct"
    KWRD_UNION      = "union"
    KWRD_ENUM       = "enum"
    KWRD_MACRO      = "macro"
    KWRD_CLASS      = "class"
    KWRD_INTERFACE  = "interface"
    KWRD_IMPLEMENTS = "implements"
    KWRD_OVERLOAD   = "overload"
    KWRD_SCOPE_PUB  = "pub"
    KWRD_SCOPE_PRIV = "priv"
    KWRD_LOOP_SKIP  = "skip"
    KWRD_LOOP_BRK   = "break"


class Token:
    def __init__(self, token_type: TokenType, literal: t.Optional[str] = None):
        self.token_type = token_type
        self.literal =  literal or repr(self.token_type.value)

    def __str__(self):
        return f"<Token: ({self.token_type}, {self.literal})>"

    def __repr__(self):
        return f"<Token: ({self.token_type}, {self.literal})>"




SYMBOLS = {
    "{": Token(TokenType.BRACKET_SQRL_L),
    "}": Token(TokenType.BRACKET_SQRL_R),
    "[": Token(TokenType.BRACKET_SQR_L),
    "]": Token(TokenType.BRACKET_SQR_R),  
    "(": Token(TokenType.BRACKET_L),
    ")": Token(TokenType.BRACKET_R),
    "'": Token(TokenType.QUOT_SINGLE),
    '"': Token(TokenType.QUOT_DOUBLE),
    ";": Token(TokenType.SEMICOL),
    ":": Token(TokenType.COLON),
    "+": Token(TokenType.PLUS),
    "*": Token(TokenType.MULT),
    "-": Token(TokenType.MINUS),
    "=": Token(TokenType.ASSIGN),
    "@": Token(TokenType.AAT),
    ",": Token(TokenType.COMA),         
    ".": Token(TokenType.DOT),
    ">": Token(TokenType.GT),
    "<": Token(TokenType.LT),
    "/" :  Token(TokenType.SLASH ), 
    "\\":  Token(TokenType.BSLASH), 
    "#" :  Token(TokenType.HASHT ), 
    "!" :  Token(TokenType.EXMARK), 
    "?" :  Token(TokenType.QMARK ), 
    "&" :  Token(TokenType.AMPER ), 
#    "\n": Token(TokenType.NEWLINE),
}


KEYWORDS = {
    "try"        : Token(TokenType.KWRD_TRY        ),
    "var"        : Token(TokenType.KWRD_VAR        ),
    "ret"        : Token(TokenType.KWRD_RET        ),
    "use"        : Token(TokenType.KWRD_USE        ),
    "func"       : Token(TokenType.KWRD_FUNC       ),
    "struct"     : Token(TokenType.KWRD_STRUCT     ),
    "union"      : Token(TokenType.KWRD_UNION      ),
    "enum"       : Token(TokenType.KWRD_ENUM       ),
    "macro"      : Token(TokenType.KWRD_MACRO      ),
    "class"      : Token(TokenType.KWRD_CLASS      ),
    "interface"  : Token(TokenType.KWRD_INTERFACE  ),
    "implements" : Token(TokenType.KWRD_IMPLEMENTS ),
    "overload"   : Token(TokenType.KWRD_OVERLOAD   ),
    "pub"        : Token(TokenType.KWRD_SCOPE_PUB  ),
    "priv"       : Token(TokenType.KWRD_SCOPE_PRIV ),
    "skip"       : Token(TokenType.KWRD_LOOP_SKIP  ),
    "break"      : Token(TokenType.KWRD_LOOP_BRK   ),
}

SCOPES = {
    "pub"        : Token(TokenType.KWRD_SCOPE_PUB  ),
    "priv"       : Token(TokenType.KWRD_SCOPE_PRIV ),
}

TYPES = {
    "int8"   : Token(TokenType.TYPE_INT8    ),
    "int16"  : Token(TokenType.TYPE_INT16   ),
    "int32"  : Token(TokenType.TYPE_INT32   ),
    "uint8"  : Token(TokenType.TYPE_UINT8   ),
    "uint16" : Token(TokenType.TYPE_UINT16  ),
    "uint32" : Token(TokenType.TYPE_UINT32  ),
    "float32": Token(TokenType.TYPE_FLOAT32 ),
    "float64": Token(TokenType.TYPE_FLOAT64 ),
    "string" : Token(TokenType.TYPE_STRING  ),
    "call"   : Token(TokenType.TYPE_CALLABLE),
    "bool"   : Token(TokenType.TYPE_BOOL    ),
    "null"   : Token(TokenType.TYPE_NULL    ),
}


class Tokenizer:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.position = 0
        self.char = self.input_string[self.position]
        self._is_indent = False

    def next_token(self):
        if self.position >= len(self.input_string):
            return Token(TokenType.EOF)

        self.char = self.input_string[self.position]
        if self.char in SYMBOLS:
            self.position += 1
            if self.char == "\n":
                self._is_indent = True
            return SYMBOLS[self.char]
        if self.is_whitespace(self.char):
            self.position += 1
            return self.next_token()
        if self.is_letter(self.char):
            return self.build_word()
        if self.is_number(self.char):
            return self.build_number()

        self.position += 1
        return Token(TokenType.ILLEGAL, self.char)

    def build_word(self):
        word = ""
        while self.is_identifier(self.char):
            word += self.char
            self.position += 1
            if self.position >= len(self.input_string): break
            self.char = self.input_string[self.position]

        if word in KEYWORDS:
            return KEYWORDS[word]
        if word in TYPES:
            return TYPES[word]
        return Token(TokenType.NAME, word)

    def build_number(self):
        num = ""
        while self.is_number(self.char):
            num += self.char
            self.position += 1
            if self.position >= len(self.input_string): break
            self.char = self.input_string[self.position]
        return Token(TokenType.NUMBER, num)
    
    def is_valid_indentation(self, indent):
        return (len(indent)%4 == 0 or len(indent)%2 == 0) and len(indent) > 0

    def is_whitespace(self, char):
        return char in [" ", "\t", "\r", "\n"]

    def is_letter(self, char):
        return char in alph+"_"

    def is_identifier(self, char):
        return self.is_number(char) or self.is_letter(char)

    def is_number(self, char):
        return char in (str(n) for n in range(10))

