from .Node import Node


class IteratorNode(Node):
    def __init__(self):
        super().__init__('Iterator')

    def evaluate(self, symbol_table):
        while self.children[0].evaluate(symbol_table)():
            self.children[1].evaluate(symbol_table)
