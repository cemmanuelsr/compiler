from .Token import Token


class ParenthesisToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)


class OpenParenthesisToken(ParenthesisToken):
    def __init__(self) -> None:
        super().__init__('(')

    @property
    def type(self) -> str:
        return 'OPEN PARENTHESIS'


class CloseParenthesisToken(ParenthesisToken):
    def __init__(self) -> None:
        super().__init__(')')

    @property
    def type(self) -> str:
        return 'CLOSE PARENTHESIS'
