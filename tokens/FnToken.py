from .Token import Token


class FnToken(Token):
    def __init__(self) -> None:
        super().__init__('fn')

    @property
    def type(self) -> str:
        return 'FN'
