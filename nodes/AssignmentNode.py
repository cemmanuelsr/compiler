from .Node import Node
from symbol_tables import symbol_table


class AssignmentNode(Node):
    def __init__(self):
        super().__init__('=')

    def evaluate(self):
        return f'''
            ; {self.children[0].value} = {self.children[1].value}
            MOV EBX, {self.children[1].evaluate()}
            MOV [EBP-{symbol_table.get(self.children[0].value)}], EBX
        '''
