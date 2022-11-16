from .Node import Node
from symbol_tables import symbol_table


class IdentifierNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        return f'[EBP-{symbol_table.get(self.value)}] ; {self.value}'
