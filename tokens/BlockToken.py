from .Token import Token


class BlockToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)


class OpenBlockToken(BlockToken):
    def __init__(self) -> None:
        super().__init__('Open Block')

    @property
    def type(self) -> str:
        return 'OPEN BLOCK'


class CloseBlockToken(BlockToken):
    def __init__(self) -> None:
        super().__init__('Close Block')

    @property
    def type(self) -> str:
        return 'CLOSE BLOCK'
