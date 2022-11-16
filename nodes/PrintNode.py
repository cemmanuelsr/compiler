from .Node import Node
from .IntegerNode import IntegerNode
from .IdentifierNode import IdentifierNode


class PrintNode(Node):
    def __init__(self):
        super().__init__('Print')

    def evaluate(self):
        if isinstance(self.children[0], (IntegerNode, IdentifierNode)):
            return f'''
                MOV EBX, {self.children[0].evaluate()}
            
                PUSH EBX
                CALL print
                POP EBX
            '''
        return f'''
            {self.children[0].evaluate()}
            
            PUSH EBX
            CALL print
            POP EBX
        '''
