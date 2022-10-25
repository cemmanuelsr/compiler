from .Token import Token


class DotToken(Token):
    def __init__(self) -> None:
        super().__init__('.')

    @property
    def type(self) -> str:
        return 'DOT'
