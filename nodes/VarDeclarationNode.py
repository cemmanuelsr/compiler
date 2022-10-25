from .Node import Node
from symbol_tables import symbol_table
from dataclasses.Type import Type


class VarDeclarationNode(Node):
    def __init__(self, cast_function):
        super().__init__('VarDec')
        self.cast_function = cast_function

    def evaluate(self):
        for child in self.children:
            symbol_table.create(child.value, Type(0 if self.cast_function == int else '', self.cast_function))
