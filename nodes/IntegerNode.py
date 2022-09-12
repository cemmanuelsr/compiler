from .Node import Node


class IntegerNode(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self):
        return self.value
