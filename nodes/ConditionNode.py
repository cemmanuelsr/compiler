from .Node import Node


class ConditionNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        if self.value == 'Else':
            self.children[0].evaluate(symbol_table)
        elif self.children[0].evaluate(symbol_table)():
            self.children[1].evaluate(symbol_table)
        elif len(self.children) > 2:
            self.children[2].evaluate(symbol_table)
