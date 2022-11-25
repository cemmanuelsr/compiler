from .Token import Token


class ReturnToken(Token):
    def __init__(self) -> None:
        super().__init__('return')

    @property
    def type(self) -> str:
        return 'RETURN'
