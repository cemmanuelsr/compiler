from .Token import Token


class OperatorToken(Token):
    def __init__(self) -> None:
        super().__init__(-1)


class PlusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '+'


class MinusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '-'


class MultToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '*'


class DivToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__()

    @property
    def type(self) -> str:
        return '/'
