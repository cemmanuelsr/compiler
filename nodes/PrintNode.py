from .Node import Node


class PrintNode(Node):
    def __init__(self):
        super().__init__('Print')

    def evaluate(self):
        return f'''
            {self.children[0].evaluate()}
            
            PUSH EBX
            CALL print
            POP EBX
        '''
