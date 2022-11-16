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
                IMUL EBX
                MOV EBX, EAX
            '''
        if self.value == '/':
            return f'''
                ; {self.children[0].value} / {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                IDIV EBX
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
                CALL binop_je
            '''
        if self.value == '>':
            return f'''
                ; {self.children[0].value} > {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                CMP EAX, EBX
                CALL binop_jg
            '''
        if self.value == '<':
            return f'''
                ; {self.children[0].value} < {self.children[1].value}
                {self.children[0].evaluate()}
                PUSH EBX
                {self.children[1].evaluate()}
                POP EAX
                CMP EAX, EBX
                CALL binop_jl
            '''
