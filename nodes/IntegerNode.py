from .Node import Node
from dataclasses.Variable import Type


class IntegerNode(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return Type(self.value, int)
