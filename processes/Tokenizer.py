from tokens.Token import Token
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken, AndToken, OrToken, NotToken, EqualToken, \
    GreaterThenToken, LessThenToken, CupToken
from tokens.NumericToken import NumericToken
from tokens.EOFToken import EOFToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BracketToken import OpenBracketToken, CloseBracketToken
from tokens.AssignmentToken import AssignmentToken
from tokens.ToToken import ToToken
from tokens.IdentifierToken import IdentifierToken
from tokens.FunctionToken import WriteToken, ReadToken
from tokens.BlockToken import OpenBlockToken, CloseBlockToken
from tokens.ConditionalToken import IfToken, ElseToken
from tokens.LoopToken import IterationToken
from tokens.ColonToken import ColonToken
from tokens.CommaToken import CommaToken
from tokens.HatToken import HatToken
from tokens.StringToken import StringToken
from tokens.ReturnToken import ReturnToken

func_token_map = {
    'Write': WriteToken,
    'Read': ReadToken,
    'Iterator': IterationToken,
    'If': IfToken,
    'Else': ElseToken,
    'return': ReturnToken
}


class Tokenizer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.position = 0
        self.next = None

    def see_next(self) -> (Token, int):
        position = self.position
        next = self.next
        c = self.source[position]
        str_size = len(self.source)
        if c.isspace() or c == '\n':
            i = position
            while i < str_size and (c.isspace() or c == '\n'):
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            position = i

        if c.isalpha():
            i = position
            name = c
            while i < str_size and (c.isalpha() or c.isdigit() or c == '_'):
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
                    name += c
            name = name[:-1]
            position = i
            functions = func_token_map.keys()

            if name in functions:
                next = func_token_map[name]()
            else:
                next = IdentifierToken(name)
        elif c == '"':
            position += 1
            c = self.source[position]
            i = position
            name = c
            while i < str_size and (c != '"'):
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
                    name += c
            name = name[:-1]
            position = i+1

            next = StringToken(name)
        elif c == '^':
            next = HatToken()
            position += 1
        elif c == '+':
            next = PlusToken()
            position += 1
        elif c == '-':
            if position + 1 < str_size and self.source[position + 1] == '>':
                next = ToToken()
                position += 2
            else:
                next = MinusToken()
                position += 1
        elif c == '*':
            next = MultToken()
            position += 1
        elif c == '/':
            next = DivToken()
            position += 1
        elif c == '&':
            next = AndToken()
            position += 1
        elif c == '|':
            next = OrToken()
            position += 1
        elif c == '!':
            next = NotToken()
            position += 1
        elif c == '(':
            next = OpenParenthesisToken()
            position += 1
        elif c == ')':
            next = CloseParenthesisToken()
            position += 1
        elif c == '{':
            next = OpenBracketToken()
            position += 1
        elif c == '}':
            next = CloseBracketToken()
            position += 1
        elif c == '\\':
            if position + 1 < str_size:
                if self.source[position + 1] == '[':
                    next = OpenBlockToken()
                    position += 2
                elif self.source[position + 1] == ']':
                    next = CloseBlockToken()
                    position += 2
                else:
                    raise Exception('Invalid token')
            else:
                raise Exception('Invalid token')
        elif c == '=':
            next = EqualToken()
            position += 1
        elif c == '>':
            next = GreaterThenToken()
            position += 1
        elif c == '<':
            if position + 1 < str_size and self.source[position + 1] == '-':
                next = AssignmentToken()
                position += 2
            else:
                next = LessThenToken()
                position += 1
        elif c == '.':
            next = CupToken()
            position += 1
        elif c == ',':
            next = CommaToken()
            position += 1
        elif c == ':':
            next = ColonToken()
            position += 1
        elif c == '\0':
            next = EOFToken()
        elif c.isdigit():
            n = ''
            i = position
            while i < str_size and c.isdigit():
                n += c
                i += 1
                if i <= str_size - 1:
                    c = self.source[i]
            position = i
            next = NumericToken(int(n))
        else:
            raise Exception('Invalid token')

        return next, position

    def select_next(self) -> None:
        self.next, self.position = self.see_next()
