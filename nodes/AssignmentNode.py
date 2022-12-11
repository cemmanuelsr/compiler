from .Node import Node


class AssignmentNode(Node):
    def __init__(self):
        super().__init__('<-')

    def evaluate(self, symbol_table):
        symbol_table.set(self.children[0].value, self.children[1].evaluate(symbol_table))
