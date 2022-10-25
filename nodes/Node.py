from dataclasses.List import List
from dataclasses.Type import Type
from processes.WriteDotFile import Writer


class Node:
    def __init__(self, value):
        self.value = value
        self.children = List(self)
        Writer.create_node_name(self)

    def evaluate(self) -> Type:
        ...
