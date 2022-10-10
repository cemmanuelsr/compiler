from .Token import Token


class NumericToken(Token):
    def __init__(self, value: int) -> None:
        super().__init__(value)

    @property
    def type(self) -> str:
        return 'NUMBER'
