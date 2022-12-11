from .Token import Token


class ToToken(Token):
    def __init__(self) -> None:
        super().__init__('->')

    @property
    def type(self) -> str:
        return 'TO'
