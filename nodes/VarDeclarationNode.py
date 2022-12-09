from .Node import Node
from dataclasses.Variable import Variable


class VarDeclarationNode(Node):
    def __init__(self, cast_function=None):
        super().__init__('VarDec')
        self.cast_function = cast_function

    def evaluate(self, symbol_table):
        for child in self.children:
            symbol_table.create(child.value, Variable(0 if self.cast_function == int else '', self.cast_function))