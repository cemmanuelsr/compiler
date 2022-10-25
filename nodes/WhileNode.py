from .Node import Node


class WhileNode(Node):
    def __init__(self):
        super().__init__('While')

    def evaluate(self):
        while self.children[0].evaluate()():
            self.children[1].evaluate()
