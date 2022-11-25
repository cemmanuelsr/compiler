from .Node import Node


class BlockNode(Node):
    def __init__(self):
        super().__init__('Block')

    def evaluate(self, symbol_table):
        for child in self.children:
            if child is not None:
                to_return = child.evaluate(symbol_table)

        if self.value != 'Root':
            return to_return