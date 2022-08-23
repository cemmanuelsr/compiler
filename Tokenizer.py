from Token import Token


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
            self.next = Token('PLUS', -1)
            self.position += 1
        if c == '-':
            self.next = Token('MINUS', -1)
            self.position += 1
        if c == '\0':
            self.next = Token('EOF', -1)
        if c.isdigit():
            n = ''
            i = self.position
            while i < str_size and c.isdigit():
                n += c
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            self.position = i
            self.next = Token('INT', int(n))
