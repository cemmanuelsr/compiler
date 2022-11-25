from .Node import Node


class ReturnNode(Node):
    def __init__(self):
        super().__init__('Return')

    def evaluate(self, symbol_table):
        return self.children[0].evaluate(symbol_table)
