from .Node import Node
from symbol_tables import symbol_table


class VarDeclarationNode(Node):
    def __init__(self):
        super().__init__('VarDec')

    def evaluate(self):
        for child in self.children:
            symbol_table.create(child.value)
        return f'''
            PUSH DWORD 0
        '''
