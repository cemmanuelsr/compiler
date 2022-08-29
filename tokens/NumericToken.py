from .Token import Token


class NumericToken(Token):
    def __init__(self, value: int) -> None:
        super().__init__('NUM', value)
