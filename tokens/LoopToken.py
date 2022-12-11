from .Token import Token


class LoopToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)


class IterationToken(LoopToken):
    def __init__(self) -> None:
        super().__init__('Iterator')

    @property
    def type(self) -> str:
        return 'ITERATION'
