from .Node import Node
from dataclasses.Type import Type
from processes.Assembler import Assembler


class IntegerNode(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self):
        Assembler.body += f'MOV EBX, {self.value}\n'
        return Type(self.value, int)
