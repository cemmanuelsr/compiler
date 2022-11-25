from .Node import Node


class WhileNode(Node):
    def __init__(self):
        super().__init__('While')

    def evaluate(self, symbol_table):
        while self.children[0].evaluate(symbol_table)():
            self.children[1].evaluate(symbol_table)
