from .Node import Node


class ReadNode(Node):
    def __init__(self):
        super().__init__('Read')

    def evaluate(self):
        return int(input(''))
