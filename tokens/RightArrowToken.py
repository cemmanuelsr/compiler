from .Token import Token


class RightArrowToken(Token):
    def __init__(self) -> None:
        super().__init__('->')

    @property
    def type(self) -> str:
        return 'RIGHT ARROW'
