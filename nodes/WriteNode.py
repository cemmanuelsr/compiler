from .Node import Node


class WriteNode(Node):
    def __init__(self):
        super().__init__('Write')

    def evaluate(self, symbol_table):
        print(self.children[0].evaluate(symbol_table)())
