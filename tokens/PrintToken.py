from .Token import Token


class PrintToken(Token):
    def __init__(self) -> None:
        super().__init__(-1)

    @property
    def type(self) -> str:
        return 'PRINT'
