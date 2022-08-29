from .Token import Token


class OperatorToken(Token):
    def __init__(self, type: str) -> None:
        super().__init__(type, -1)


class PlusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('+')


class MinusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('-')


class MultToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('*')


class DivToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('/')
