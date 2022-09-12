from .Node import Node


class UnaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == '+':
            return self.children[0].evaluate()
        if self.value == '-':
            return -self.children[0].evaluate()
