from .Node import Node


class IdentifierNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return symbol_table.get(self.value)
