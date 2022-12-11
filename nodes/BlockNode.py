from .Node import Node


class BlockNode(Node):
    def __init__(self):
        super().__init__('Block')

    def evaluate(self, symbol_table):
        for child in self.children:
            if child is not None:
                if child.value == 'Return':
                    return child.evaluate(symbol_table)
                child.evaluate(symbol_table)
        