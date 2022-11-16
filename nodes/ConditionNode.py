from .Node import Node


class ConditionNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        if self.value == 'Else':
            return f'''
                ; else
                {self.children[0].evaluate()}
            '''
        elif len(self.children) > 2:
            return f'''
                {self.children[2].evaluate()}
            '''
        else:
            return f'''
                ; if 
                CONDITION_{self.id}:

                {self.children[0].evaluate()}

                CMP EBX, False
                JE EXIT_{self.id}

                {self.children[1].evaluate()}

                JMP CONDITION_{self.id}
                EXITC_{self.id}
            '''
