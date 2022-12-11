from .Token import Token


class HatToken(Token):
    def __init__(self) -> None:
        super().__init__('^')

    @property
    def type(self) -> str:
        return 'HAT'
