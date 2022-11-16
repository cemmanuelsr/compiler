from .Node import Node


class BinaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == '+':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                ADD EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '-':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '*':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                MUL EBX
                MOV EBX, EAX
            '''
        if self.value == '/':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                DIV EBX
                MOV EBX, EAX
            '''
        if self.value == '&&':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                AND EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '||':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                OR EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '==':
            return f'''
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                JE EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '>':
            return self.children[0].evaluate() > self.children[1].evaluate()
        if self.value == '<':
            return self.children[0].evaluate() < self.children[1].evaluate()
        if self.value == '.':
            return self.children[0].evaluate().__concat__(self.children[1].evaluate())
