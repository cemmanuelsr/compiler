from .Node import Node


class BinaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        left_evaluate = self.children[0].evaluate()
        right_evaluate = self.children[1].evaluate()
        if (self.value != '.') and (left_evaluate.cast_function != int or right_evaluate.cast_function != int):
            raise Exception(
                f'Unsupported operation {self.value} between {left_evaluate.cast_function} and {right_evaluate.cast_function}')
        if self.value == '+':
            return self.children[0].evaluate() + self.children[1].evaluate()
        if self.value == '-':
            return self.children[0].evaluate() - self.children[1].evaluate()
        if self.value == '*':
            return self.children[0].evaluate() * self.children[1].evaluate()
        if self.value == '/':
            return self.children[0].evaluate() // self.children[1].evaluate()
        if self.value == '&&':
            return self.children[0].evaluate() & self.children[1].evaluate()
        if self.value == '||':
            return self.children[0].evaluate() | self.children[1].evaluate()
        if self.value == '==':
            return self.children[0].evaluate() == self.children[1].evaluate()
        if self.value == '>':
            return self.children[0].evaluate() > self.children[1].evaluate()
        if self.value == '<':
            return self.children[0].evaluate() < self.children[1].evaluate()
        if self.value == '.':
            return self.children[0].evaluate().__concat__(self.children[1].evaluate())
