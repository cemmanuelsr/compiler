from .Node import Node


class BlockNode(Node):
    def __init__(self):
        super().__init__('Block')

    def evaluate(self):
        asm = ''
        for child in self.children:
            if child is not None:
                asm += child.evaluate()

        return asm
