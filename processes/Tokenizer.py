from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken
from tokens.NumericToken import NumericToken
from tokens.EOFToken import EOFToken


class Tokenizer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.position = 0
        self.next = None

    def select_next(self) -> None:
        c = self.source[self.position]
        str_size = len(self.source)
        if c.isspace():
            i = self.position
            while i < str_size and c.isspace():
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            self.position = i
        if c == '+':
            self.next = PlusToken()
            self.position += 1
        elif c == '-':
            self.next = MinusToken()
            self.position += 1
        elif c == '*':
            self.next = MultToken()
            self.position += 1
        elif c == '/':
            self.next = DivToken()
            self.position += 1
        elif c == '\0':
            self.next = EOFToken()
        elif c.isdigit():
            n = ''
            i = self.position
            while i < str_size and c.isdigit():
                n += c
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            self.position = i
            self.next = NumericToken(int(n))
        else:
            raise Exception('Invalid token')
