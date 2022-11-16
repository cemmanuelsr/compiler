from .Node import Node
from .IntegerNode import IntegerNode
from .IdentifierNode import IdentifierNode


class BinaryOpNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == '+':
            return f'''
                ; {self.children[0].value} + {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                ADD EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '-':
            return f'''
                ; {self.children[0].value} - {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                SUB EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '*':
            return f'''
                ; {self.children[0].value} * {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                MUL EBX
                MOV EBX, EAX
            '''
        if self.value == '/':
            return f'''
                ; {self.children[0].value} / {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                DIV EBX
                MOV EBX, EAX
            '''
        if self.value == '&&':
            return f'''
                ; {self.children[0].value} && {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                AND EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '||':
            return f'''
                ; {self.children[0].value} || {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                OR EAX, EBX
                MOV EBX, EAX
            '''
        if self.value == '==':
            return f'''
                ; {self.children[0].value} == {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                CMP EAX, EBX
                JE EQUALITY_{self.id}
                MOV EBX, 0
                EQUALITY_{self.id}:
                MOV EBX, 1
            '''
        if self.value == '>':
            return f'''
                ; {self.children[0].value} > {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                CMP EAX, EBX
                JG EQUALITY_{self.id}
                MOV EBX, 0
                EQUALITY_{self.id}:
                MOV EBX, 1
            '''
        if self.value == '<':
            return f'''
                ; {self.children[0].value} < {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                CMP EAX, EBX
                JL EQUALITY_{self.id}
                MOV EBX, 0
                EQUALITY_{self.id}:
                MOV EBX, 1
            '''
