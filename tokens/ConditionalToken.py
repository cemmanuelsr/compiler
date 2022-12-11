from .Token import Token


class ConditionalToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)


class IfToken(ConditionalToken):
    def __init__(self) -> None:
        super().__init__('If')

    @property
    def type(self) -> str:
        return 'IF'


class ElseToken(ConditionalToken):
    def __init__(self) -> None:
        super().__init__('Else')

    @property
    def type(self) -> str:
        return 'ELSE'
