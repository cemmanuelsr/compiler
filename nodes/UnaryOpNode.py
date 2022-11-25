from .Node import Node


class UnaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        if self.value == '+':
            return self.children[0].evaluate(symbol_table)
        if self.value == '-':
            return -self.children[0].evaluate(symbol_table)
        if self.value == '!':
            return self.children[0].evaluate(symbol_table).__not__()
