from .Node import Node
from dataclasses.Variable import Variable


class ReadNode(Node):
    def __init__(self):
        super().__init__('Read')

    def evaluate(self, symbol_table):
        return Variable(int(input('')), int)
