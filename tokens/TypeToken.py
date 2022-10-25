from .Token import Token


class TypeToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)

    @property
    def type(self) -> str:
        return 'TYPE'
