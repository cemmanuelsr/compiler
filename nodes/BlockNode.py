from .Node import Node


class BlockNode(Node):
    def __init__(self):
        super().__init__('Block')

    def evaluate(self):
        for child in self.children:
            if child is not None:
                child.evaluate()
