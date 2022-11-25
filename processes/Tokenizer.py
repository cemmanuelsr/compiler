from tokens.Token import Token
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken, AndToken, OrToken, NotToken, EqualToken, \
    GreaterThenToken, LessThenToken
from tokens.NumericToken import NumericToken
from tokens.EOFToken import EOFToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BracketToken import OpenBracketToken, CloseBracketToken
from tokens.AssignmentToken import AssignmentToken
from tokens.IdentifierToken import IdentifierToken
from tokens.FunctionToken import PrintToken, ReadToken
from tokens.SemicolonToken import SemicolonToken
from tokens.ConditionalToken import IfToken, ElseToken
from tokens.LoopToken import WhileToken
from tokens.ColonToken import ColonToken
from tokens.CommaToken import CommaToken
from tokens.DotToken import DotToken
from tokens.TypeToken import TypeToken
from tokens.VarDeclarationToken import VarDeclarationToken
from tokens.StringToken import StringToken
from tokens.FnToken import FnToken
from tokens.RightArrowToken import RightArrowToken
from tokens.ReturnToken import ReturnToken

func_token_map = {
    'Print': PrintToken,
    'Read': ReadToken,
    'while': WhileToken,
    'if': IfToken,
    'else': ElseToken,
    'var': VarDeclarationToken,
    'i32': TypeToken,
    'String': TypeToken,
    'fn': FnToken,
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
                if name == 'i32':
                    next = func_token_map[name]('i32')
                elif name == 'String':
                    next = func_token_map[name]('String')
                else:
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
        elif c == '+':
            next = PlusToken()
            position += 1
        elif c == '-':
            if position + 1 < str_size and self.source[position + 1] == '>':
                next = RightArrowToken()
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
            if position + 1 < str_size and self.source[position + 1] == '&':
                next = AndToken()
                position += 2
            else:
                raise Exception('Invalid syntax')
        elif c == '|':
            if position + 1 < str_size and self.source[position + 1] == '|':
                next = OrToken()
                position += 2
            else:
                raise Exception('Invalid syntax')
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
        elif c == ';':
            next = SemicolonToken()
            position += 1
        elif c == '=':
            if position + 1 < str_size and self.source[position + 1] == '=':
                next = EqualToken()
                position += 2
            else:
                next = AssignmentToken()
                position += 1
        elif c == '>':
            next = GreaterThenToken()
            position += 1
        elif c == '<':
            next = LessThenToken()
            position += 1
        elif c == '.':
            next = DotToken()
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
