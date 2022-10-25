from .Token import Token


class StringToken(Token):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    @property
    def type(self) -> str:
        return 'STRING'
