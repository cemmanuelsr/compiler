from .Node import Node


class PrintNode(Node):
    def __init__(self):
        super().__init__(None)

    def evaluate(self):
        print(self.children[0].evaluate())
