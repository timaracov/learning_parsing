#def p(input_string: str):
#    stack = []
#    pos = 0
#
#    while True:
#        if pos >= len(input_string):
#            break
#
#        char = input_string[pos]
#        if char in SYMBOLS:
#            stack.append(SYMBOLS[char].name)
#        elif char.isspace():
#            stack.append((Token.WHITESPACE.name, char))
#        elif char.isdecimal():
#            decimal = []
#            while char.isdecimal():
#                decimal.append(char)
#                pos += 1
#                char = input_string[pos]
#            pos -= 1
#
#            num_word = "".join(decimal)
#            stack.append((Token.DECIMAL.name, num_word))
#        elif char in alph:
#            ident = []
#            while char in alph:
#                ident.append(char)
#                pos += 1
#                char = input_string[pos]
#            pos -= 1
#
#            word = "".join(ident)
#            if word in KEYWORDS:
#                stack.append(KEYWORDS[word].name)
#            else:
#                stack.append((Token.IDENT.name, word))
#        else:
#            stack.append((Token.ILLEGAL.name, char))
#        pos += 1
#
#    return stack


