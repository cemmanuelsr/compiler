from .Node import Node
from symbol_tables import symbol_table
from processes.Assembler import Assembler


class AssignmentNode(Node):
    def __init__(self):
        super().__init__('=')

    def evaluate(self):
        symbol_table.set(self.children[0].value, self.children[1].evaluate())
        Assembler.body += f'''
            MOV EBX, {self.children[1].evaluate().value}
            MOV [EBP-{symbol_table.get(self.children[0].value)[1]}], EBX
        '''
