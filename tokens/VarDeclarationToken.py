from .Token import Token


class VarDeclarationToken(Token):
    def __init__(self) -> None:
        super().__init__('var')

    @property
    def type(self) -> str:
        return 'VAR DECLARATION'
