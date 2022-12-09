from .Node import Node
from dataclasses.Variable import Variable


class StringNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return Variable(self.value, str)
