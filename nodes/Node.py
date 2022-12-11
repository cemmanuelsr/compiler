from dataclasses.Variable import Type


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, symbol_table) -> Type:
        ...
