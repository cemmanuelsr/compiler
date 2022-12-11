from .Token import Token


class OperatorToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)


class PlusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('+')

    @property
    def type(self) -> str:
        return 'PLUS'


class MinusToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('-')

    @property
    def type(self) -> str:
        return 'MINUS'


class MultToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('*')

    @property
    def type(self) -> str:
        return 'MULTIPLICATION'


class DivToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('/')

    @property
    def type(self) -> str:
        return 'DIVISION'


class AndToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('&')

    @property
    def type(self) -> str:
        return 'AND'


class OrToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('|')

    @property
    def type(self) -> str:
        return 'OR'


class NotToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('!')

    @property
    def type(self) -> str:
        return 'NOT'


class EqualToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('=')

    @property
    def type(self) -> str:
        return 'EQUAL'


class GreaterThenToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('>')

    @property
    def type(self) -> str:
        return 'GREATER THEN'


class LessThenToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('<')

    @property
    def type(self) -> str:
        return 'LESS THEN'


class CupToken(OperatorToken):
    def __init__(self) -> None:
        super().__init__('.')

    @property
    def type(self) -> str:
        return 'CONCAT'
