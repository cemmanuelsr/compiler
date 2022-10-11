from .Node import Node


class ConditionNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == 'Else':
            self.children[0].evaluate()
        elif self.children[0].evaluate():
            self.children[1].evaluate()
        elif len(self.children) > 2:
            self.children[2].evaluate()
