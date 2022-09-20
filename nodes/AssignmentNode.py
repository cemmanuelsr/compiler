from .Node import Node
from symbol_tables import symbol_table


class AssignmentNode(Node):
    def __init__(self):
        super().__init__(None)

    def evaluate(self):
        symbol_table.set(self.children[0].value, self.children[1].evaluate())
