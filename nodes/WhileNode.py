from .Node import Node


class WhileNode(Node):
    def __init__(self):
        super().__init__('While')

    def evaluate(self):
        return f'''
            LOOP_{self.id}:
            
            {self.children[0].evaluate()}
            
            CMP EBX, False
            JE EXIT_{self.id}
            
            {self.children[1].evaluate()}
            
            JMP LOOP_{self.id}
            EXITL_{self.id}
        '''
