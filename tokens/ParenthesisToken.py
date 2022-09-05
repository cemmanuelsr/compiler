from .Token import Token


class ParenthesisToken(Token):
    def __init__(self) -> None:
        super().__init__(-1)


class OpenParenthesisToken(ParenthesisToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '('


class CloseParenthesisToken(ParenthesisToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return ')'
