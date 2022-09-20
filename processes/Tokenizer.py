from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken
from tokens.NumericToken import NumericToken
from tokens.EOFToken import EOFToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BracketToken import OpenBracketToken, CloseBracketToken
from tokens.AssignmentToken import AssignmentToken
from tokens.IdentifierToken import IdentifierToken
from tokens.PrintToken import PrintToken
from tokens.SemicolonToken import SemicolonToken

func_token_map = {
    'Print': PrintToken
}


class Tokenizer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.position = 0
        self.next = None

    def select_next(self) -> None:
        c = self.source[self.position]
        str_size = len(self.source)
        if c.isspace() or c == '\n':
            i = self.position
            while i < str_size and (c.isspace() or c == '\n'):
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            self.position = i

        if c.isalpha():
            i = self.position
            name = c
            while i < str_size and (c.isalpha() or c.isdigit() or c == '_'):
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
                    name += c
            name = name[:-1]
            self.position = i
            functions = func_token_map.keys()

            if name in functions:
                self.next = func_token_map[name]()
            else:
                self.next = IdentifierToken(name)
        elif c == '+':
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
        elif c == '(':
            self.next = OpenParenthesisToken()
            self.position += 1
        elif c == ')':
            self.next = CloseParenthesisToken()
            self.position += 1
        elif c == '{':
            self.next = OpenBracketToken()
            self.position += 1
        elif c == '}':
            self.next = CloseBracketToken()
            self.position += 1
        elif c == ';':
            self.next = SemicolonToken()
            self.position += 1
        elif c == '=':
            self.next = AssignmentToken()
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
