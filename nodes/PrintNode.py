from .Node import Node
from processes.Assembler import Assembler


class PrintNode(Node):
    def __init__(self):
        super().__init__('Print')

    def evaluate(self):
        Assembler.body += f'''
            MOV EBX, {self.children[0].evaluate().value}

            PUSH EBX
            CALL print
            POP EBX
        '''
