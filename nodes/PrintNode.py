from .Node import Node


class PrintNode(Node):
    def __init__(self):
        super().__init__('Print')

    def evaluate(self, symbol_table):
        print(self.children[0].evaluate(symbol_table)())
