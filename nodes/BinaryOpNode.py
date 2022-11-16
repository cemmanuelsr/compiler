from .Node import Node


class BinaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == '+':
            return f'''
                ; {self.children[0].value} + {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                ADD EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '-':
            return f'''
                ; {self.children[0].value} - {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '*':
            return f'''
                ; {self.children[0].value} * {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                MUL EBX
                MOV EBX, EAX
            '''
        if self.value == '/':
            return f'''
                ; {self.children[0].value} / {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                DIV EBX
                MOV EBX, EAX
            '''
        if self.value == '&&':
            return f'''
                ; {self.children[0].value} && {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                AND EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '||':
            return f'''
                ; {self.children[0].value} || {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                OR EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '==':
            return f'''
                ; {self.children[0].value} == {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                CMP EAX, 0
                MOV EBX, ZF
            '''
        if self.value == '>':
            return f'''
                ; {self.children[0].value} > {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                CMP 0, EAX
                MOV EBX, CF
            '''
        if self.value == '<':
            return f'''
                ; {self.children[0].value} < {self.children[1].value}
                MOV EBX, {self.children[0].evaluate()}
                PUSH EBX
                MOV EBX, {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                CMP EAX, 0
                MOV EBX, CF
            '''
