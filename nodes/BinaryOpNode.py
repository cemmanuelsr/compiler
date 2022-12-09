from .Node import Node
from .IntegerNode import IntegerNode
from .IdentifierNode import IdentifierNode


class BinaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        if self.value == '+':
            return self.children[0].evaluate(symbol_table) + self.children[1].evaluate(symbol_table)
        if self.value == '-':
            return self.children[0].evaluate(symbol_table) - self.children[1].evaluate(symbol_table)
        if self.value == '*':
            return self.children[0].evaluate(symbol_table) * self.children[1].evaluate(symbol_table)
        if self.value == '/':
            return self.children[0].evaluate(symbol_table) // self.children[1].evaluate(symbol_table)
        if self.value == '&&':
            return self.children[0].evaluate(symbol_table) & self.children[1].evaluate(symbol_table)
        if self.value == '||':
            return self.children[0].evaluate(symbol_table) | self.children[1].evaluate(symbol_table)
        if self.value == '==':
            return self.children[0].evaluate(symbol_table) == self.children[1].evaluate(symbol_table)
        if self.value == '>':
            return self.children[0].evaluate(symbol_table) > self.children[1].evaluate(symbol_table)
        if self.value == '<':
            return self.children[0].evaluate(symbol_table) < self.children[1].evaluate(symbol_table)
        if self.value == '.':
            return self.children[0].evaluate(symbol_table).__concat__(self.children[1].evaluate(symbol_table))
