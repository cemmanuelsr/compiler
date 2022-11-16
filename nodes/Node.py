from dataclasses.List import List
from processes.WriteDotFile import Writer
from dataclasses.IdGiver import IdGiver


class Node:
    def __init__(self, value):
        self.id = IdGiver.counter
        IdGiver.counter += 1
        self.value = value
        self.children = List(self)
        Writer.create_node_name(self)

    def evaluate(self) -> str:
        ...
