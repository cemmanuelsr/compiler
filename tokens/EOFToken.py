from .Token import Token


class EOFToken(Token):
    def __init__(self) -> None:
        super().__init__('\0')

    @property
    def type(self) -> str:
        return 'EOF'
