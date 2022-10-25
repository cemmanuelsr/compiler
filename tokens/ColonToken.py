from .Token import Token


class ColonToken(Token):
    def __init__(self) -> None:
        super().__init__(':')

    @property
    def type(self) -> str:
        return 'COLON'
