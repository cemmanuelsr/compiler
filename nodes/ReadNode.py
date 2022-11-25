from .Node import Node
from dataclasses.Variable import Type


class ReadNode(Node):
    def __init__(self):
        super().__init__('Read')

    def evaluate(self, symbol_table):
        return Type(int(input('')), int)
