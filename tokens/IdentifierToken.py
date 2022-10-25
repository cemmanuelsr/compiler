from .Token import Token


class IdentifierToken(Token):
    def __init__(self, value=None) -> None:
        super().__init__(value)

    @property
    def type(self) -> str:
        return 'IDENTIFIER'
