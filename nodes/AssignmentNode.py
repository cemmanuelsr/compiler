from .Node import Node
from symbol_tables import symbol_table


class AssignmentNode(Node):
    def __init__(self):
        super().__init__('=')

    def evaluate(self):
        symbol_table.create(self.children[0].value, self.children[1].evaluate())
        return f'''
            PUSH DWORD 0
            MOV EBX, {self.children[1].evaluate()}
            MOV [EBP-{symbol_table.get(self.children[0].value)}], EBX
        '''
