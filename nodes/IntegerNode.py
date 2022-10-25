from .Node import Node
from dataclasses.Type import Type


class IntegerNode(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self):
        return Type(self.value, int)
