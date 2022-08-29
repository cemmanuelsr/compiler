from .Token import Token


class EOFToken(Token):
    def __init__(self) -> None:
        super().__init__('EOF', -1)
