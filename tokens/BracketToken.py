from .Token import Token


class BracketToken(Token):
    def __init__(self) -> None:
        super().__init__(-1)


class OpenBracketToken(BracketToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '{'


class CloseBracketToken(BracketToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '}'
