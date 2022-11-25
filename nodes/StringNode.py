from .Node import Node
from dataclasses.Variable import Type


class StringNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return Type(self.value, str)
