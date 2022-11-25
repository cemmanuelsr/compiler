from .Node import Node


class NoOpNode(Node):
    def __init__(self):
        super().__init__('[NULL]')

    def evaluate(self, symbol_table):
        pass
