from .Node import Node
from symbol_tables import symbol_table
from processes.Assembler import Assembler


class IdentifierNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self):
        Assembler.body += f'MOV EBX, [EBP-{symbol_table.get(self.value)[1]}]'
        return symbol_table.get(self.value)[0]
