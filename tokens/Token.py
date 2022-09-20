class Token:
    def __init__(self, value) -> None:
        self.value = value

    def type(self) -> str:
        ...
