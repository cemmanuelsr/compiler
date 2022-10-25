from .Node import Node
from dataclasses.Type import Type


class ReadNode(Node):
    def __init__(self):
        super().__init__('Read')

    def evaluate(self):
        return Type(int(input('')), int)
