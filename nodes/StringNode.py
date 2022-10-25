from .Node import Node
from dataclasses.Type import Type


class StringNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        return Type(self.value, str)
