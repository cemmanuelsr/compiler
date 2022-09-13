class Token:
    def __init__(self, value: int) -> None:
        self.value = value

    def type(self) -> str:
        ...
