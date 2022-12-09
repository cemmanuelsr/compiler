from .Node import Node
from tables import func_table
from dataclasses.Function import Function


class FuncDecNode(Node):
    def __init__(self, value, type=None):
        super().__init__(value)
        self.type = type

    def evaluate(self, symbol_table):
        func_table.create(self.value, Function(self.type, self))
